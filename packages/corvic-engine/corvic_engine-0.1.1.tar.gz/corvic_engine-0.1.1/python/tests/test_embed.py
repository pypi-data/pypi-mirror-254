from collections.abc import Generator, Sequence
from dataclasses import dataclass
from typing import Any, cast

import fastnode2vec
import numpy as np
import numpy.typing as npt
import pandas as pd
import pytest
from numpy.typing import NDArray
from scipy.spatial import distance

from corvic.embed import node2vec


def cosine(
    embeddings_x: NDArray[np.float32], embeddings_y: NDArray[np.float32]
) -> float:
    """Compute the cosine distance between two embeddings spaces."""
    assert embeddings_x.shape == embeddings_y.shape
    average_x = np.mean(embeddings_x, axis=1)
    average_y = np.mean(embeddings_y, axis=1)
    return float(distance.cosine(average_x, average_y))


def embed_space(keyed_vector: Any):
    entity_emb = {}
    for key in keyed_vector.index_to_key:
        entity_emb[str(key)] = keyed_vector[key]
    emb = pd.DataFrame(entity_emb)
    return cast(npt.NDArray[np.float32], emb.to_numpy())  # pyright: ignore


@dataclass
class _Node2VecParam:
    dim: int
    walk_length: int
    window: int
    p: float
    q: float
    epochs: int
    edges: Sequence[tuple[int, int]]


def _generate_edges(n: int, k: int) -> Generator[tuple[int, int], None, None]:
    for _ in range(k):
        src = np.random.permutation(np.arange(stop=np.int32(n), dtype=np.int32))  # pyright: ignore  # noqa: NPY002
        dst = np.random.permutation(np.arange(stop=np.int32(n), dtype=np.int32))  # pyright: ignore  # noqa: NPY002
        for i in range(n):
            yield src[i], dst[i]


def run_fastnode2vec(param: _Node2VecParam):
    graph = fastnode2vec.Graph(
        param.edges,
        directed=True,
        weighted=False,
    )
    n2v = fastnode2vec.Node2Vec(
        graph=graph,
        dim=param.dim,
        walk_length=param.walk_length,
        window=param.window,
        p=param.p,
        q=param.q,
        workers=1,
    )
    n2v.train(  # pyright: ignore[reportUnknownMemberType]
        epochs=param.epochs,
    )

    return embed_space(n2v.wv)


def run_node2vec(param: _Node2VecParam):
    space = node2vec.Space(
        param.edges,
        directed=True,
    )
    n2v = node2vec.Node2Vec(
        space=space,
        dim=param.dim,
        walk_length=param.walk_length,
        window=param.window,
        p=param.p,
        q=param.q,
        workers=1,
    )
    n2v.train(
        epochs=param.epochs,
    )

    return embed_space(n2v.keyed_vectors)


def test_node2vec():
    param = _Node2VecParam(
        dim=10,
        walk_length=10,
        window=10,
        p=2,
        q=1,
        epochs=50,
        edges=list(_generate_edges(n=100, k=100)),
    )

    run_node2vec(param)


@pytest.mark.skip(reason="numerical comparisons are too unstable")
def test_node2vec_quality():
    param = _Node2VecParam(
        dim=10,
        walk_length=10,
        window=10,
        p=2,
        q=1,
        epochs=50,
        edges=list(_generate_edges(n=100, k=100)),
    )

    out1 = run_node2vec(param)
    out2 = run_node2vec(param)
    out3 = run_fastnode2vec(param)
    out4 = run_fastnode2vec(param)
    rng = np.random.default_rng(seed=1)
    out_random = rng.random((10, 100), dtype=np.float32)

    assert cosine(out1, out4) == pytest.approx(0.0, abs=1e-1)  # pyright: ignore[reportUnknownMemberType]
    assert cosine(out3, out4) == pytest.approx(0.0, abs=1e-1)  # pyright: ignore[reportUnknownMemberType]
    assert cosine(out1, out2) == pytest.approx(0.0, abs=1e-1)  # pyright: ignore[reportUnknownMemberType]
    assert cosine(out1, out_random) != pytest.approx(0.0, abs=1e-1)  # pyright: ignore[reportUnknownMemberType]
    assert cosine(out3, out_random) != pytest.approx(0.0, abs=1e-1)  # pyright: ignore[reportUnknownMemberType]

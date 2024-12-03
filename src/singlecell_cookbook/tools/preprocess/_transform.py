from typing import Literal, Optional

from anndata import AnnData


def pool_neighbors(
    adata: AnnData,
    layer: Optional[str] = None,
    n_neighbors: Optional[int] = None,
    pooling_mode: Literal["connectivity", "adjacency"] = "adjacency",
    neighbors_key: Optional[str] = None,
    key_added: Optional[str] = None,
    overwrite: bool = False,
) -> None:
    raise NotImplementedError

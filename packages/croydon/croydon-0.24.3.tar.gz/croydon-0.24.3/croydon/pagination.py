import asyncio
import math
from time import time
from typing import Generic, List, Callable, Awaitable, Optional
from pydantic import BaseModel
from .types import TModel, T
from .db import ObjectsCursor
from . import ctx


class ItemList(BaseModel, Generic[T]):
    data: List[T]


class PaginatedList(ItemList, Generic[T]):
    count: int
    page: int
    total_pages: int


class PaginationParams(BaseModel):
    page: int
    limit: int


async def paginated(
    cur: ObjectsCursor[TModel],
    *,
    transform: Callable[[TModel], Awaitable[T]],
    params: Optional[PaginationParams] = None,
) -> ItemList[T] | PaginatedList[T]:
    t1 = time()
    if params is None:
        items = await cur.all()
        tasks = [transform(x) for x in items]
        data = await asyncio.gather(*tasks)
        ctx.log.debug(
            f"paginated {cur.ctor.__self__.__name__} list with no_paging took %.3f secs",
            time() - t1,
        )
        return ItemList(data=data)

    offset = (params.page - 1) * params.limit
    total_count = await cur.count()
    total_pages = math.ceil(total_count / params.limit)
    cur = cur.skip(offset).limit(params.limit)
    items = await cur.all()
    tasks = [transform(x) for x in items]
    data = await asyncio.gather(*tasks)
    ctx.log.debug(
        f"paginated {cur.ctor.__self__.__name__} list with limit={params.limit} took %.3f secs",
        time() - t1,
    )
    return PaginatedList(
        count=total_count, page=params.page, total_pages=total_pages, data=data
    )


async def pagination_params(
    page: int = 1, limit: Optional[int] = None, no_paging: bool = False
) -> Optional[PaginationParams]:
    if no_paging:
        return None
    if limit is None:
        limit = ctx.cfg.general.documents_per_page
    return PaginationParams(page=page, limit=limit)

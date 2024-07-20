from typing import Optional, Union

from fastapi import APIRouter
from starlette import status

from backend.Dto.request.CreateNewsRequest import CreateNewsRequest

router = APIRouter(
    prefix='/news',
)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_news(nid: Optional[int] = None, offset: int = 0, limit: int = 10):
    return {"News": "123"}


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_news(news: CreateNewsRequest):
    return news


@router.put("/", status_code=status.HTTP_201_CREATED)
async def update_news():
    ...


@router.delete("/", status_code=status.HTTP_201_CREATED)
async def movie_in_archive(nid: int):
    return {'message': f"News with ID: {nid} moved in archive."}

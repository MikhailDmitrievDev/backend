from fastapi import APIRouter, FastAPI


class BaseConfig:
    """Base config API."""
    api_url = '/api/v1'

    @classmethod
    def gather_routs(cls, application: FastAPI, routs: list[APIRouter]) -> None:
        """
        Function get route from list[routs] and added in application.

        :param application: FastAPI - object application
        :param routs: List[APIRouter] - list objects APIRouter

        """
        for route in routs:
            application.include_router(route)

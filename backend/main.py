import uvicorn
from fastapi import FastAPI

from core.config import BaseConfig
from controller.rest.router import router as news_router

app = FastAPI(
    title="API Movie-RolePlay",
    description="API for Movie-RolePlay site.",
    version="0.1.0",
    root_path=BaseConfig.api_url,
    openapi_prefix=BaseConfig.api_url,
    swagger_ui_oauth2_redirect_url=BaseConfig.api_url

)

routs = [
    news_router
]

BaseConfig.gather_routs(application=app, routs=routs)

if __name__ == "__main__":
    uvicorn.run(app, port=8001)

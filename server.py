from fastapi import FastAPI

from routes import router as api_router


def get_application():
    app = FastAPI()
    app.include_router(api_router)

    return app


app = get_application()
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from endpoints import content


app = FastAPI()
app.include_router(content.router)

if __name__ == "__main__":

    @app.get("/")
    async def root():
        return {"message": "Image Optimizer Backend is running"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run("ArtEra.asgi:application", reload=True)

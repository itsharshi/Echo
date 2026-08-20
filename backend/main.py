from fastapi import FastAPI

app = FastAPI(title="Echo Backend")


@app.get("/health")
def health():
    return {"status": "ok"}

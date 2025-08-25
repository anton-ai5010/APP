from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

static_dir = Path(__file__).resolve().parent.parent / "static"
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")


@app.get("/api/health")
def health() -> dict[str, str]:
    """Simple health check endpoint."""
    return {"status": "ok"}

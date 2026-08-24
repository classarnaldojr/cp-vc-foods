from io import BytesIO
from pathlib import Path
from typing import Any

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image, UnidentifiedImageError

from model import initialize_model, predict_image

app = FastAPI(
    title="Checkpoint - Classificador de Imagens",
    description="Base FastAPI usada no checkpoint de Visão Computacional.",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_PATH = BASE_DIR / "frontend.html"

MODEL_READY = False
SETUP_ERROR: str | None = None


@app.on_event("startup")
def startup_event() -> None:
    global MODEL_READY, SETUP_ERROR
    try:
        initialize_model()
        MODEL_READY = True
        SETUP_ERROR = None
    except NotImplementedError as exc:
        MODEL_READY = False
        SETUP_ERROR = str(exc)
    except Exception as exc:
        MODEL_READY = False
        SETUP_ERROR = f"Erro ao carregar o modelo: {exc}"


@app.get("/", response_class=HTMLResponse)
def home() -> HTMLResponse:
    if not FRONTEND_PATH.exists():
        raise HTTPException(status_code=500, detail="frontend.html não encontrado")
    return HTMLResponse(FRONTEND_PATH.read_text(encoding="utf-8"))


@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok" if MODEL_READY else "incompleto",
        "modelo_carregado": MODEL_READY,
        "detalhe": SETUP_ERROR,
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> dict[str, Any]:
    if not MODEL_READY:
        raise HTTPException(
            status_code=503,
            detail="Modelo ainda não foi integrado. Complete model.py e reinicie a API.",
        )

    raw = await file.read()
    try:
        image = Image.open(BytesIO(raw)).convert("RGB")
    except UnidentifiedImageError as exc:
        raise HTTPException(status_code=400, detail="Arquivo inválido.") from exc

    try:
        result = predict_image(image)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Erro na inferência: {exc}") from exc

    return {
        "arquivo": file.filename,
        **result,
    }

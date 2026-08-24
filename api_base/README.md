# API base

Vamos usar o modelo treinado no notebook como motor dsta API.

## Teste inicial

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Antes da integração do modelo:

- `GET /health` deve responder com `modelo_carregado: false`;
- `POST /predict` deve responder `503`.

Depois de completar `model.py` e copiar seus artefatos para `artifacts/`, reinicie a API.

A interface está em:

```text
http://127.0.0.1:8000/
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

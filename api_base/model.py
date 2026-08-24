"""Integração do modelo treinado no notebook com a API.

Complete este arquivo.

A API espera duas funções públicas:

- initialize_model(): carrega arquitetura, pesos e metadados.
- predict_image(image): recebe uma PIL.Image e devolve um dicionário com a predição.

Formato mínimo esperado por predict_image():

{
    "classe_prevista": "nome_da_classe",
    "probabilidade": 0.91,
    "top3": [
        {"classe": "...", "probabilidade": 0.91},
        ...
    ]
}
"""

from typing import Any
from PIL import Image


def initialize_model() -> None:
    # TODO: carregar artefatos produzidos no notebook.
    # TODO: reconstruir/carregar a arquitetura escolhida.
    # TODO: colocar o modelo em modo de avaliação.
    raise NotImplementedError("Implemente initialize_model() em model.py")


def predict_image(image: Image.Image) -> dict[str, Any]:
    # TODO: aplicar o mesmo pré-processamento usado no treinamento.
    # TODO: executar inferência sem cálculo de gradientes.
    # TODO: converter logits em probabilidades.
    # TODO: devolver classe prevista, probabilidade e top3.
    raise NotImplementedError("Implemente predict_image() em model.py")

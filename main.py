import g4f

from pydantic import BaseModel

g4f.debug.logging = True  # mostrar mensagens de log


def create_response(prompt):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )
    return response

# setup da mais poderosa e complexa api já vista


class Mensage(BaseModel):
    prompt: str


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# configuração da API mais poderosa que já existiu

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Bem-vindo à API mais poderosa que já existiu!"}


@app.put("/prompt_mensage")
def create_mensage(mensage: Mensage):
    return create_response(mensage.prompt)

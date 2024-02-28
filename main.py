import g4f
from fastapi import FastAPI
from pydantic import BaseModel

g4f.debug.logging = True  # mostrar mensagens de log


def create_response(prompt):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )
    return response

# setup da mais poderosa e complexa api já vista


app = FastAPI()


class Mensage(BaseModel):
    prompt: str


@app.put("/prompt_mensage")
def create_mensage(mensage: Mensage):
    return create_response(mensage.prompt)

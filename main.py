from fastapi import FastAPI
from fastapi import Query
from http import HTTPStatus
from src.models.cadeira import Cadeira as Cadeira

app = FastAPI()

app.state.cadeiras_db={}

@app.get("/cadeiras/")
async def getCadeiras():
    cadeiras = "\n".join(str(cadeira) for cadeira in app.state.cadeiras_db.values())
    return cadeiras

@app.post("/cadeiras/", status_code = HTTPStatus.CREATED, response_model = Cadeira)
async def addCadeiras(cadeira: Cadeira):
    app.state.cadeiras_db[cadeira.id]=cadeira
    return cadeira

@app.put("/cadeiras/{id}" )
async def editCadeiras(id: int, cadeira: Cadeira):
    cadeiras_db =app.state.cadeiras_db
    if id in cadeiras_db:
        cadeiras_db[id] = cadeira
        return cadeiras_db[id]
    return {"mensagem": "Cadeira inexistente"}

@app.delete("/cadeiras/")
async def deleteCadeiras(id:int = Query(...)):
    try:
        app.state.cadeiras_db.pop(id)
        return {"message": "deletado com sucesso"}
    except:
        return {"mensagem": "Cadeira Inexistente"}, 204

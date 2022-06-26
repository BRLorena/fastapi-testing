from fastapi import FastAPI as api

app = api()

vendas = {
    1: {"item": "300ml", "price": 4, "qtde.": 5},
    2: {"item": "1.5L", "price": 15, "qtde.": 5},
    3: {"item": "750ml", "price": 10, "qtde.": 5},
    4: {"item": "200ml", "price": 2, "qtde.": 5},
}

size = len(vendas)


@app.get("/")
def home():
    return {"Vendas": size}


@app.get("/vendas")
def get_all_vendas():
    return vendas


@app.get("/vendas/{id_vendas}")
def get_venda(id_vendas: int):
    if id_vendas in vendas:
        return vendas[id_vendas]
    else:
        return {"Error": f"Id not found... Please enter an id between 1- {size}"}

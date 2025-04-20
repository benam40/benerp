from fastapi import FastAPI
from user import router as user_router
from crm import router as crm_router
from inventory import router as inventory_router
from pos import router as pos_router

app = FastAPI(title="Berp ERP App")

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(crm_router, prefix="/crm", tags=["CRM"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])
app.include_router(pos_router, prefix="/pos", tags=["POS"])

@app.get("/")
def root():
    return {"message": "Welcome to Berp ERP!"}

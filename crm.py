from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_customers():
    return [{"id": 1, "customer": "Acme Corp"}]

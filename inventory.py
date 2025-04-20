from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_inventory():
    return [{"id": 1, "item": "Sample Product", "qty": 100}]

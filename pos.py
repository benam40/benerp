from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_pos():
    return [{"id": 1, "sale": "POS001", "total": 50.0}]

# from ruva.utils.ApiHandler import manager
from fastapi import APIRouter

router = APIRouter(
    # prefix="/root",
    tags=["root"]
)


@router.get("/")
def welcome():
    return "Welcome to ruva"


@router.get("/ssup")
def ssup():
    return "Wassup"

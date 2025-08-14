from fastapi import FastAPI
from ruva.utils.APIUtils import GetMethods, PostMethods

app = FastAPI()

# def manager_init():
#     from ruva.utils.WorkspaceManager import WorkspaceManager
#     manager = WorkspaceManager()
#     return manager

app.include_router(GetMethods.router)
app.include_router(PostMethods.router)

from appfastapiBackend import startAmis
from fastapi import FastAPI

app=FastAPI()
startAmis(app,"/amis/get/home")

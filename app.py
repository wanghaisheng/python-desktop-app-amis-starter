from apphelper import startAmisApp
from fastapi import FastAPI

app=FastAPI()
startAmisApp(app,"/login")

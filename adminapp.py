from adminhelper import startAmisAdmin
from fastapi import FastAPI

adminapp=FastAPI()
startAmisAdmin(adminapp,"/amis/set")

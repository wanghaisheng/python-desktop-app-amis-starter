from fastapiHelperadmin import start_ui
import uvicorn
from app import app
from adminapp import adminapp

runGUI=False
mode={
  "gui_without_browser":0,
  "gui_with_browser":1,
  "browser_without_gui":2
}

if __name__ == '__main__':
  if runGUI:
    start_ui(adminapp)

  else:
    uvicorn.run("adminapp:adminapp",host="0.0.0.0",port=8090,debug=True,reload=True)

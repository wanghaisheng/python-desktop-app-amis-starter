from apphelper import start_ui
import uvicorn
from app import app
runGUI=True

if __name__ == '__main__':
  if runGUI:
    start_ui(app)

  else:
    uvicorn.run("app:app",host="0.0.0.0",port=8091,debug=True,reload=True)

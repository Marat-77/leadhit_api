from fastapi import FastAPI

from routers.forms_tmp import form_tmp

app = FastAPI()
app.include_router(form_tmp)

# запуск uvicorn:
# run uvicorn:
# uvicorn main:app --reload
#
# options: host (default '127.0.0.1'), port (default 8000):
# uvicorn main:app --reload --host 192.168.123.123 --port 8888

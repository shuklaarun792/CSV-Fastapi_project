from fastapi import FastAPI
from database import engine
import models
from routes import student   # 👈 important

# table create
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# include routes
app.include_router(student.router)


from fastapi import FastAPI, Depends
from database import engine,SessionLocal
from sqlalchemy import text
import models
from sqlalchemy.orm import Session

from routes import student   # 👈 important

# table create
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="StudentAPI")

# include routes
app.include_router(student.router)


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ DB check endpoint
@app.get("/check_db")
def check_db(db: Session = Depends(get_db)):
    try:
        # simple query
        db.execute(text("SELECT 1"))
        return {"status": "connected to database ✅"}
    except Exception as e:
        return {"status": "error ❌", "detail": str(e)}



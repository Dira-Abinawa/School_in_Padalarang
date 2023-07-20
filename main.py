from fastapi import FastAPI
from routes.schools import sch
app = FastAPI(
    title='Dira Abinawa - Schools in Padalarang',
    version='1.0.0'
)
app.include_router(sch)
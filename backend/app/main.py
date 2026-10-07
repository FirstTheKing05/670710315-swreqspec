from fastapi import FastAPI

from app.db.session import engine, init_db
from app.slots.router import router as slots_router

app = FastAPI(title='Booking API')


@app.on_event('startup')
def startup_event():
    init_db(engine)


app.include_router(slots_router)


@app.get('/health')
async def health():
    return {'status': 'ok'}

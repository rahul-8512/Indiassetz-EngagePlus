from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Indiassetz EngagePlus API 🚀")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EventCreate(BaseModel):
    title: str
    date: str
    location: str
    max_attendees: int = 100

events_db: List[dict] = []

@app.get("/")
async def root():
    return {"message": "EngagePlus API LIVE"}

@app.get("/api/events")
async def get_events():
    return events_db

@app.post("/api/events")
async def create_event(event: EventCreate):
    new_event = {
        "id": len(events_db) + 1,
        **event.dict(),
        "attendees": 0,
    }
    events_db.append(new_event)
    return new_event

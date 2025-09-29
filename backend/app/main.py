from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Guitar AI API", version="0.1.0")


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


@app.get("/heatlth", tags=["Health"])
def health_check():
    return {"status": "ok"}


@app.post("/auth/register")
def register(playload: UserCreate):
    # Registration logic will be implemented here
    return {"todo": "implement", "email": payload.email}

from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int = Field(ge=0, le=1000, default=99)
    movie: str = Field(min_length=5, max_length=25)
    category: str = Field(default="category 1")

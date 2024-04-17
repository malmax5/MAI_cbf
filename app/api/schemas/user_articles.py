from pydantic import BaseModel, constr


class UserArticle_Create(BaseModel):
    user_id: int
    book_id: int
    article_name: constr(max_length=255)
    text: constr(max_length=3000)

    class Config:
        orm_mode = True
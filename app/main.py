# app/main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from app.models.models import User, Note, Tag
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

templates = Jinja2Templates(directory="app/templates")

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.main"]},
    generate_schemas=True,
    add_exception_handlers=True,
) 


# app/main.py
from tortoise import fields
from tortoise.models import Model

class User(Model):
    id_user = fields.IntField(pk=True)
    user_name = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    
    def __str__(self):
        return self.user_name

class Note(Model):
    id_note = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at  = fields.DatetimeField(auto_now_add=True)
    is_draft = fields.BooleanField(default=True)
    is_deleted = fields.BooleanField(default=False)

    #user = fields.ForeignKeyField('models.User', related_name='notes', default=None)

    def __str__(self):
        return self.title

class Tag(Model):
    id_tag = fields.IntField(pk=True)
    content = fields.CharField(max_length=255)

    def __str__(self):
        return self.content

# class NoteHasTag(Model):
#     id_has = fields.IntField(pk=True)
#     id_note = fields.ForeignKeyField('models.Note', related_name='note_has_tag')
#     id_tag = fields.ForeignKeyField('models.Tag', related_name='note_has_tag')



class UserSchema(BaseModel):
    """docstring for User"""
    id_user : int
    user_name : str
    password : str

@app.get("/")
async def root(request: Request):
    """
    Main route of the api
    """
    return {'message':'hello world'}

@app.get("/api/v1/ressources/notes/create")
async def notes_create(request: Request):
    """
    This route create a default note with a specific content
    """
    note = await Note.create(
        title="Titre de la note",
        content="contenu de la note"
    )
    return note

@app.get("/api/v1/ressources/tags/create")
async def tags_create(request: Request):
    tag = await Tag.create(
        content="nom du tag"
    )
    return tag

@app.get("/api/v1/ressources/users/create")
async def users_create(request: Request):
    user = await User.create(
        password="mon mot de passe",
        user_name="Johnny speeder"
    )
    return user

@app.get("/api/v1/ressources/users/all")
async def users_list(request: Request):
    users = await User.all()
    return users

@app.get("/api/v1/ressources/notes/all")
async def notes_list(request: Request):
    notes = await Note.all()
    return notes

@app.get("/api/v1/ressources/tags/all")
async def tags_list(request: Request):
    tags = await Tag.all()
    return tags


@app.get("/api/v1/ressources/users")
async def user_ressource(user_name: str):
    users = await User.all()
    return {"test": user_name, 'test2':id_}

@app.get("/api/v1/ressources/notes")
async def notes_list(title: str):
    notes = await Note.all()
    return notes

@app.get("/api/v1/ressources/tags/")
async def tags_list(request: Request):
    tags = await Tag.all()
    return tags



@app.get("/api/v1/ressources/users")
async def users_list(user_name: Optional[str]):
    users = await User.all()
    return users

@app.get("/api/v1/ressources/notes")
async def notes_list(title: Optional[str]):
    notes = await Note.all()
    return notes

@app.get("/api/v1/ressources/tags")
async def tags_list(content: Optional[str]):
    return tags


@app.post("/api/v1/ressources/users2/create")
async def create_user(user: UserSchema):
    return {'new_user' : user.dict}
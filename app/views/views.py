from fastapi import APIRouter
from fastapi import Request
from app.models.models import User, Note, Tag

articles_views = APIRouter()
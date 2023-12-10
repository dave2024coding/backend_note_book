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


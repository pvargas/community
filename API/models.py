import config
import datetime
from peewee import *


DATABASE = MySQLDatabase(config.DB, host=config.HOST, port=config.PORT, user=config.USER)

class User(Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(45)	    
    member_since = DateTimeField(default=datetime.datetime.now)
    is_moderator = BooleanField(default=False)

    class Meta:
        database = DATABASE

class Post(Model):
    id = PrimaryKeyField(primary_key=True)
    author  = ForeignKeyField(User)
    title   = CharField(300)
    content = TextField(default='')
    is_url  = BooleanField()
    created_at = DateTimeField(default=datetime.datetime.now)
    last_modified = TimestampField()

    class Meta:
        database = DATABASE

class PostVotes(Model):
    post_id = ForeignKeyField(Post)
    user_id = ForeignKeyField(User)
    value = SmallIntegerField()

    class Meta:
        database = DATABASE

class Tag(Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(45)

    class Meta:
        database = DATABASE

class PostTags(Model):
    post_id = ForeignKeyField(Post)
    tag_id  = ForeignKeyField(Tag)

    class Meta:
        database = DATABASE

class Comment(Model):
    id = PrimaryKeyField(primary_key=True)
    parent = ForeignKeyField('self')
    author  = ForeignKeyField(User)
    post = ForeignKeyField(Post)
    content = TextField()    
    created_at = DateTimeField(default=datetime.datetime.now)
    last_modified = TimestampField()

    class Meta:
        database = DATABASE

class CommentVotes(Model):
    comment_id = ForeignKeyField(Comment)
    user_id = ForeignKeyField(User)
    value = SmallIntegerField()

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post, Tag, Comment, PostVotes, CommentVotes, PostTags], safe=True)
    DATABASE.close()

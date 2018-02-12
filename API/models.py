import datetime

from peewee import *
from marshmallow_peewee import ModelSchema
from playhouse.migrate import *

from config import Database as config

DATABASE = MySQLDatabase(config.DB, host=config.HOST,
                         port=config.PORT, user=config.USER, password=config.PAS)
migrator = MySQLMigrator(DATABASE)


class User(Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(45, unique=True)
    member_since = DateTimeField(
        constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    is_moderator = BooleanField(constraints=[SQL('DEFAULT FALSE')])

    class Meta:
        database = DATABASE


class Post(Model):
    id = PrimaryKeyField(primary_key=True)
    author = ForeignKeyField(User)
    title = CharField(300)
    is_url = BooleanField()
    content = TextField()
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    last_modified = DateTimeField(
        constraints=[SQL('ON UPDATE CURRENT_TIMESTAMP')])

    class Meta:
        database = DATABASE


class PostVotes(Model):
    post_id = ForeignKeyField(Post)
    user_id = ForeignKeyField(User)
    value = SmallIntegerField()

    class Meta:
        database = DATABASE
        primary_key = CompositeKey('post_id', 'user_id')


class Tag(Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(45, unique=True)

    class Meta:
        database = DATABASE


class PostTags(Model):
    post_id = ForeignKeyField(Post)
    tag_id = ForeignKeyField(Tag)

    class Meta:
        database = DATABASE
        primary_key = CompositeKey('post_id', 'tag_id')


class Comment(Model):
    id = PrimaryKeyField(primary_key=True)
    parent = ForeignKeyField('self', related_name='children', null=True)
    author = ForeignKeyField(User)
    post = ForeignKeyField(Post)
    content = TextField()
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    last_modified = DateTimeField(
        constraints=[SQL('ON UPDATE CURRENT_TIMESTAMP')],null=True)

    class Meta:
        database = DATABASE


class CommentVotes(Model):
    comment_id = ForeignKeyField(Comment)
    user_id = ForeignKeyField(User)
    value = SmallIntegerField()

    class Meta:
        database = DATABASE
        primary_key = CompositeKey('comment_id', 'user_id')


# Schema for all the above classes


class UserSchema(ModelSchema):

    class Meta:
        model = User


class PostSchema(ModelSchema):

    class Meta:
        model = Post


class PostVotesSchema(ModelSchema):

    class Meta:
        model = PostVotes


class TagSchema(ModelSchema):

    class Meta:
        model = Tag


class PostTagsSchema(ModelSchema):

    class Meta:
        model = PostTags


class CommentSchema(ModelSchema):

    class Meta:
        model = Comment


class CommentVotesSchema(ModelSchema):

    class Meta:
        model = CommentVotes


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post, Tag, Comment, PostVotes,
                            CommentVotes, PostTags], safe=True)
    migrate(
        # Make `posts` allow NULL values.
        # migrator.drop_not_null('post', 'last_modified')
    )
    DATABASE.close()

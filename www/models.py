import time, uuid
from www.orm import Model, StringField, BooleanField, FloatField, TextField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)
# 主键id的缺省值是函数next_id，创建时间created_at的缺省值是函数time.time，可以自动设置当前日期和时间。
#
# 日期和时间用float类型存储在数据库中，而不是datetime类型，
# 这么做的好处是不必关心数据库的时区以及时区转换问题，
# 排序非常简单，显示的时候，只需要做一个float到str的转换，也非常容易。

# 建表
# create table users (
#     `id` varchar(50) not null,
#     `email` varchar(50) not null,
#     `passwd` varchar(50) not null,
#     `admin` bool not null,
#     `name` varchar(50) not null,
#     `image` varchar(500) not null,
#     `created_at` real not null,
#     unique key `idx_email` (`email`),
#     key `idx_created_at` (`created_at`),
#     primary key (`id`)
# ) engine=innodb default charset=utf8;
#
# create table blogs (
#     `id` varchar(50) not null,
#     `user_id` varchar(50) not null,
#     `user_name` varchar(50) not null,
#     `user_image` varchar(500) not null,
#     `name` varchar(50) not null,
#     `summary` varchar(200) not null,
#     `content` mediumtext not null,
#     `created_at` real not null,
#     key `idx_created_at` (`created_at`),
#     primary key (`id`)
# ) engine=innodb default charset=utf8;
#
# create table comments (
#     `id` varchar(50) not null,
#     `blog_id` varchar(50) not null,
#     `user_id` varchar(50) not null,
#     `user_name` varchar(50) not null,
#     `user_image` varchar(500) not null,
#     `content` mediumtext not null,
#     `created_at` real not null,
#     key `idx_created_at` (`created_at`),
#     primary key (`id`)
# ) engine=innodb default charset=utf8;

' url handlers '
import re, time, json, logging, hashlib, base64, asyncio
from www.coroweb import get
from www.models import User, Comment, Blog, next_id


@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
# Web框架的设计是完全从使用者出发，目的是让使用者编写尽可能少的代码。
#
# 编写简单的函数而非引入request和web.Response还有一个额外的好处，
# 就是可以单独测试，否则，需要模拟一个request才能测试。
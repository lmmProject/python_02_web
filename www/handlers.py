' url handlers '
from www.coroweb import get
from www.models import User


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
# Web框架的设计是完全从使用者出发，目的是让使用者编写尽可能少的代码。
#
# 编写简单的函数而非引入request和web.Response还有一个额外的好处，
# 就是可以单独测试，否则，需要模拟一个request才能测试。
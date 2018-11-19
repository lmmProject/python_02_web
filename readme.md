# 实战
## 搭建环境
异步框架aiohttp：
$pip3 install aiohttp  
前端模板引擎jinja2：
$ pip3 install jinja2  
MySQL的Python异步驱动程序aiomysql：
$ pip3 install aiomysql  
## 异步编程
由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作，因为所有用户都是由一个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。而耗时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户。  
这就是异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”。幸运的是aiomysql为MySQL数据库提供了异步IO的驱动  
## cookie认证登陆
由于HTTP协议是一种无状态协议，而服务器要跟踪用户状态，就只能通过cookie实现。大多数Web框架提供了Session功能来封装保存用户状态的cookie。  
##### Session
优点是简单易用，可以直接从Session中取出用户登录信息。  
Session的缺点是服务器需要在内存中维护一个映射表来存储用户登录信息，如果有两台以上服务器，就需要对Session做集群，因此，使用Session的Web App很难扩展。  
##### cookie
每次用户访问任意URL，都会对cookie进行验证，这种方式的好处是保证服务器处理任意的URL都是无状态的，可以扩展到多台服务器。  
由于登录成功后是由服务器生成一个cookie发送给浏览器，所以，要保证这个cookie不会被客户端伪造出来。  
实现防伪造cookie的关键是通过一个单向算法（例如SHA1），举例如下：  
当用户输入了正确的口令登录成功后，服务器可以从数据库取到用户的id，并按照如下方式计算出一个字符串：  
__"用户id" + "过期时间" + SHA1("用户id" + "用户口令" + "过期时间" + "SecretKey")__  
当浏览器发送cookie到服务器端后，服务器可以拿到的信息包括：  
用户id  
过期时间  
SHA1值  
如果未到过期时间，服务器就根据用户id查找用户口令，并计算：  
__SHA1("用户id" + "用户口令" + "过期时间" + "SecretKey")__   
并与浏览器cookie中的哈希进行比较，如果相等，则说明用户已登录，否则，cookie就是伪造的。  
这个算法的关键在于**SHA1是一种单向算法**，即可以通过原始字符串计算出SHA1结果，但无法通过SHA1结果反推出原始字符串。  
## doctest
doctest是python自带的一个模块，你可以把它叫做“文档测试”（doctest）模块。  
doctest的使用有两种方式：一个是嵌入到python源中。另一个是放到一个独立文件。  


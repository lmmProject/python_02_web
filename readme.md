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

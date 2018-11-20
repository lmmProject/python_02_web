"""
    $ pip3 install watchdog
"""
import os, sys, time, subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Django的开发环境在Debug模式下就可以做到自动重新加载，如果我们编写的服务器也能实现这个功能，就能大大提升开发效率。
# 其实Python本身提供了重新载入模块的功能，但不是所有模块都能被重新载入。
# 另一种思路是检测www目录下的代码改动，一旦有改动，就自动重启服务器。
# Python的第三方库watchdog可以利用操作系统的API来监控目录文件的变化，并发送通知
# 利用Python自带的subprocess实现进程的启动和终止，并把输入输出重定向到当前进程的输入输出中：
def log(s):
    print('[Monitor] %s' % s)


class MyFileSystemEventHander(FileSystemEventHandler):
    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: %s' % event.src_path)
            self.restart()


command = ['echo', 'ok']
process = None


def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with code %s.' % process.returncode)
        process = None


def start_process():
    global process, command
    log('Start process %s...' % ''.join(command))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


def restart_process():
    kill_process()
    start_process()


def start_watch(path, callback):
    observer = Observer();
    observer.schedule(MyFileSystemEventHander(restart_process), path, recursive=True)
    observer.start()
    log('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    # argv = sys.argv[1:]
    # if not argv:
    #     print('Usage: ./pymonitor your-script.py')
    #     exit(0)
    # if argv[0] != 'python':
    #     argv.insert(0, 'python')
    command = 'python app.py'
    path = os.path.abspath('.')
    start_watch(path, None)


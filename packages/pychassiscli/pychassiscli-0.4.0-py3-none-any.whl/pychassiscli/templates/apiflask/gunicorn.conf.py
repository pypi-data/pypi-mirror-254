import multiprocessing

from gevent import monkey

monkey.patch_all()

bind = "0.0.0.0:5000"
worker_class = 'gevent'
# 设置最大并发量
daemon = False
debug = False
worker_connections = 12
workers = multiprocessing.cpu_count() * 2 + 1
# timeout = 120 

# 指定每个工作者的线程数
# threads = 10

# pidfile = "/var/run/gunicorn.pid"
# accesslog = '/var/log/gunicorn_access.log'
# errorlog = '/var/log/gunicorn_error.log'
# 设置日志记录水平
loglevel = 'warning'
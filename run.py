from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', 'utf-8')
https = int(config.get('aio_push', 'https'))

if https == 0:
    from mylib.http_async_push_v1 import Http
    demo = Http()
    demo.start()
else:
    from mylib.https_async_push import Https
    demo = Https()
    demo.start()

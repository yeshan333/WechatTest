# -*- coding: utf-8 -*-
# file:name
import web
from handle import Handle

urls = (
    '/wx', 'Handle',
)

# 去除
""" class Handle(object):
    def GET(self):
        return "hello, this is a test" """

if __name__ == '__main__':
    # 创建一个列举这些url的application
    app = web.application(urls, globals())
    app.run()



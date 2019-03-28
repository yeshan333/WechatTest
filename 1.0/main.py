# -*- coding: utf-8 -*-
# file:name
import web

urls = (
    '/wx', 'Handle',
)

class Handle(object):
    def GET(self):
        return "hello, this is a test"

if __name__ == '__main__':
    # 创建一个列举这些url的application
    app = web.application(urls, globals())
    app.run()



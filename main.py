#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from pymongo import MongoClient


urls = (
    '/', 'index',
    '/TodoLists', 'todo.TD',
    '/TodoLists/(\w+)', 'todo.TD_Simple',
    '/renderTest', 'Test',
    # '/add','add',

)
render = web.template.render('templates')

class Test:
    def GET(self):
        return render.showRender('hello world')


from pymongo import MongoClient

# Making a Connection with MongoClient
client = MongoClient('localhost', 27017)
# Getting a Database
db = client['todo_db']
# Getting a Collection
collection = db['TodoLists']

class index:
    def GET(self):
        return "欢迎来到待办事项首页!"
config = web.storage(
    email='piaosanlang@gmail.com',
    site_name = '任务跟踪',
    site_desc = '',
    static = '/static',
)
web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
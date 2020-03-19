#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import module1
import markdown
import psycopg2
# from pymongo import MongoClient


urls = (
    '/', 'index',
    '/add', 'add',
    # '/hello_1[/]?.*', 'hello_1',
    '/(.*)','hello',


)
app = web.application(urls, globals())

# globals = {'markdown': markdown.markdown}
render = web.template.render('templates',builtins={},base="layout",globals={'m1':module1})
# Making a Connection with MongoClient

db = web.database(
    dbn='postgres',
    host='localhost',
    port=5432,
    user='postgres',
    pw='641229',
    # db='postgres',
    db='test',
)

class index:
    def GET(self):
        todos = db.select('todo')
        return render.index_2(todos)

        # return 'Hello, '+name+'!'
    def POST(self):
        i = web.input()
        print(i)

class add:

    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        web.seeother('/')


class hello:
    def GET(self,name):
        i = web.input(times=1)
        if not name:
            name = 'world'
        for c in range(int(i.times)):
            print('hello',name,'!')

        return 'Hello, '+name+'!'
    def POST(self):
        i = web.input()
        print(i)

#
class hello_1:

    def GET(self):

        return render.index_1('Lisa')



class hello_2:

    def GET(self, name):
        return render.index_2(name)
class add:
    def POST(self):
        i = web.input(name=[])
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')
# post_data=web.input(name=[])

# client = MongoClient('localhost', 27017)
# db = client.todo_db
# collection = db['TodoLists']

if __name__ == "__main__":

#     render = web.template.render('templates')
#     print('hello')
    app.run()
#     print(render.index('hello'))


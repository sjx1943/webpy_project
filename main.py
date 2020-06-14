#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import web

urls = (
    '/article','article',
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello',
)

render = web.template.render('templates')

# from pymongo import MongoClient



class index:
    def GET(self):
        query = web.input()
        # return query
        return web.seeother('/article')



class blog:
    def POST(self):
        data = web.input()
        return data
    def GET(self):
        return web.ctx.env


class hello:
    def GET(self,name):
        return render.hello_1(name)

class article:
    def GET(self):

        con = pymysql.connect('localhost', 'root',
                              '19910403Sjx@', 'web_learning')

        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM test")
        except:
            con.ping()
            cur = con.cursor()
            cur.execute("SELECT * FROM test")
        rows = cur.fetchall()
        cur.close()
        con.close()

        print(rows)
        return render.article(rows)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
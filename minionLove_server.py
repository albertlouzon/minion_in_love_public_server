import os
from os import environ as env
from sys import argv

import bottle as b
from bottle import default_app, request, route, response, get

@route('/')
def index():
    return b.template('minecraft.html')


@get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return b.static_file(filename, root='js')

@get('/css/<filename:re:.*\.css>')
def javascript(filename):
    return b.static_file(filename, root='css')


@get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def img(filename):
    return b.static_file(filename, root='img')

@get('/sounds/<filename:re:.*\.mp3>')
def javascript(filename):
    return b.static_file(filename, root='sounds')

def main():
     bottle.run(host='0.0.0.0', port=argv[1])
p

if __name__ == '__main__':
    main()

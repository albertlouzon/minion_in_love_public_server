from bottle import route, run, get, static_file, response, request
import bottle as b


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
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()

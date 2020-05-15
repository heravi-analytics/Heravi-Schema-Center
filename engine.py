from bottle import route, jinja2_view, run, template, response
import functools
import json

from SchemaHandler import SchemaHandler

view = functools.partial(jinja2_view, template_lookup=['templates'])
schemas = SchemaHandler().loadSchemas()


@route('/', method="GET", name="home")
@view('home.html')
def index():
    return {}


@route('/schema/name_all', method="GET", name="")
def getSchemas():
    schemasName = {'schemas': list(schemas.keys())}
    response.content_type = 'application/json'
    return json.dumps(schemasName)


run(host='localhost', port=1350)

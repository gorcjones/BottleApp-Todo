import sqlite3
from bottle import route, run, debug, template

@route('/todo')
def toto_list():
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	c.close()
	output = template('make_table', rows=result)
	return output
	
debug(True)
run(reloader=True)
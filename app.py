from bottle import route,static_file,run,template
import sqlite3
@route('/')
def index():
   return static_file('index.html',root='')

@route('/clients')
def clients():
   conn = sqlite3.connect('data.db')
   c = conn.cursor()
   c.execute("SELECT id, sitename, client,phone,info FROM orders")
   result = c.fetchall()
   c.close()
   output = template('clients.html', rows=result)
   return output
   

#Runner
run(host='0.0.0.0',port=5150,debug=True,reloader=True)
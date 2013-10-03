import web
import simplejson
import btserial as bt

app = web.application(('/',  'Index'), globals())
render = web.template.render('templates/')

def send_handler(message):
	return message
	
def connect_handler(message):
	print message['content']
	return message

def disconnect_handler(message):
	return message
	
class Index(object):
	
	def GET(self):
		link = web.input(name='main')
		exec('result = render.%s()'%(link.name))
		return result

	def POST(self):
		message = simplejson.loads(web.data())			
		if message['command'] in ('send', 'connect', 'disconnect'):
			exec('result = %s_handler(message)'%(message['command']))
			return result

if __name__ == "__main__": app.run()

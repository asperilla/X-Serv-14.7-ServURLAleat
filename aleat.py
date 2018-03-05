#!/usr/bin/python3

import webapp
import random

class AleatApp(webapp.webApp):

	def parse(self, request):
		try:
			return request.split()[1]
		except IndexError:
			return None
	
	def process(self, parsedRequest):
		
		print(parsedRequest)
		numero = str(random.randint(0, 3122332432))

		respuesta = '<a href=' + "http://localhost:4567/" + numero + '>' + "Dame otra"
		return ("200 OK", "<html><body><p>Hola. " + respuesta + "</p></body></html>")

if __name__ == "__main__":
	testWebApp = AleatApp("localhost", 4567)

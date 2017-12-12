# -*- coding: utf-8 -*-

# Return the client application
class Root(Resource):
	def get(self):
		return app.send_static_file('index.html')

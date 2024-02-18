from .network import Connect
from requests import get
import json
class Api_GetContents:
	def __init__(self,user,passw,name):
		self.username = user
		self.method = Connect(user, passw)
		self.name = name
	@property
	def text(self) -> str:
		 return get('https://arver.ir/' + self.username + '/api/' + self.name + '.json').text
	def json(self) -> dict:
		return get('https://arver.ir/' + self.username + '/api/' + self.name + '.json').json()
class Client:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.method = Connect(username, password)
	def addApi(self, name, data):
		return self.method.send_request('add', {'api_name': name, 'data':data})
	def getApis(self):
		return self.method.send_request('apis', {})
	def signup(self, email, username, password):
		return Connect(username, password).send_request('create_acc', {'email': email})
	def deleteApi(self, name):
		return self.method.send_request('delete_api', {'api_name':name})
	def editApi(self, name, data):
		return self.method.send_request('edit_api', {'api_name':name, 'data':data})
	def getData(self, name):
		return Api_GetContents(self.username, self.password, name)
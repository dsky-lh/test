import　hashlib
import　web
import　lxml
import　time
import　os
import　urllib2
import　json
from　lxml import etree

class WeixinInterface:
	def GET(self):
		data = web.input()
		signature = data.signature
		timestamp = data.timestamp
		nonce = data.nonce
		token = 'qlife'
		echostr = data.echostr

		list = [token,timestamp,nonce]
		list.sort()
		list2 = ''.join(list)
		sha1 = hashlib.sha1()
		sha1.update(list2.encode('utf-8'))
		hashcode = sha1.hexdigest()

		if hashcode == signature:
			return echostr
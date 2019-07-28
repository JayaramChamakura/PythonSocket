import Server
import unittest
import socket as tsocket
class TestSocketServer(unittest.TestCase):
	def setUp(self):
		self.port=9090
		self.socketObj=Server.CustomSocket('cineserver',self.port)
	def test_server_settings(self):
		self.assertEqual(self.socketObj.hostname,'cineserver')
		self.assertEqual(self.socketObj.port,self.port)
	def test_socket(self):
		ssock=(self.socketObj.createSock())
		assert ssock.family == tsocket.AF_INET


if __name__ == '__main__':
    unittest.main()

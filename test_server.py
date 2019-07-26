import Server
import unittest
import socket as tsocket
class TestSocketServer(unittest.TestCase):
	def setUp(self):
		self.socketObj=Server.CustomSocket('cineserver',11001)
	def test_server_settings(self):
		self.assertEqual(self.socketObj.hostname,'cineserver')
		self.assertEqual(self.socketObj.port,11001)
	def test_socket(self):
		ssock=(self.socketObj.createSock())
		assert ssock.family == tsocket.AF_INET


if __name__ == '__main__':
    unittest.main()

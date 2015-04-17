from nose import with_setup
from snoopy import server
import unittest
import json

class SnoopyServerTestCase(unittest.TestCase):
	def setUp(self):
		server.app.config['TESTING'] = True
		self.app = server.app.test_client()

	def tearDown(self):
		pass

	def test_info(self):
		response = self.app.get("/info")
		assert response.status_code == 200
		assert json.loads(response.data)['status'] == 'Alive!'

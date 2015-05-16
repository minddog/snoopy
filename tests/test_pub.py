from nose import with_setup
import unittest
import json
from snoopy import pub

class PubTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_secret(self):
        pub.SECRETS['test-stream'] = 'secret'
        response = pub.create_authorized_stream('test-stream', 'secret')
        assert response.invalid == True


    def test_valid_secret(self):
        pub.SECRETS['*'] = '05fcb9ae971da4434ffb86a652ec8606'
        response = pub.create_authorized_stream('test-stream', pub.sign_secret('secret'))
        assert response.invalid == False

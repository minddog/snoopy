from snoopy import schema
import mock

def test_responder_default():
    response = schema.Responder(mock.MagicMock(), _protocol="default")
    response.parser = mock.MagicMock()
    response.respond('test')
    response.parser.assert_called()
    response.logger.debug.assert_called()

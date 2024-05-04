from tests.test_sns_handler import SnsHandlerLambdaTestCase


class TestSuccess(SnsHandlerLambdaTestCase):

    def test_success(self):
        event = {
            'Records': [
                {
                    'body': 'test'
                }
            ]
        }
        self.assertEqual(self.HANDLER.handle_request(event, dict()), 200)


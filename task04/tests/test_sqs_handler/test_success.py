from tests.test_sqs_handler import SqsHandlerLambdaTestCase


class TestSuccess(SqsHandlerLambdaTestCase):

    def test_success(self):
        event = {
            'Records': [
                {
                    'body': 'test'
                }
            ]
        }
        self.assertEqual(self.HANDLER.handle_request(event, dict()), 200)

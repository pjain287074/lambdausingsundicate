from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import boto3

_LOG = get_logger('SqsHandler-handler')


class SqsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Handle SQS event
        """
        message = event['Records'][0]['body']
        # Print the message to CloudWatch Logs
        print('SQS Message: ', message)
        return 200


HANDLER = SqsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
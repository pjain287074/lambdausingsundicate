from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

# _LOG = get_logger('SnsHandler-handler')


class SnsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Handle SNS event
        """
        message = event['Records'][0]['body']
        # Print the message to CloudWatch Logs
        print(message)
        return 200



HANDLER = SnsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)

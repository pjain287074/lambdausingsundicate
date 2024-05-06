import datetime
import json
import uuid
import boto3
from boto3.dynamodb.conditions import Key
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('AuditProducer-handler')
dynamodb = boto3.resource('dynamodb')

class AuditProducer(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        audit_table = dynamodb.Table('Audit')

        for record in event['Records']:
            new_image = record['dynamodb']['NewImage']

            item_key = new_image['key']['S']
            new_value = int(new_image['value']['N'])

            audit_data = {
                "id": str(uuid.uuid4()),
                "itemKey": item_key,
                "modificationTime": datetime.datetime.now().isoformat(),
                "newValue": {
                    "key": item_key,
                    "value": new_value
                }
            }

            if record['eventName'] == 'MODIFY':
                old_image = record['dynamodb']['OldImage']
                old_value = int(old_image['value']['N'])

                if old_value != new_value:
                    audit_data["updatedAttribute"] = "value"
                    audit_data["oldValue"] = old_value

            print(f"Creating audit record for item: {item_key}")
            audit_table.put_item(Item=audit_data)

        return 200


HANDLER = AuditProducer()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)

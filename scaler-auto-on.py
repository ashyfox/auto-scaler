'''
import base64

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
'''




import base64
import google.auth
from pprint import pprint
from googleapiclient import discovery
from google.oauth2 import service_account
from oauth2client.client import GoogleCredentials
print("## 111111111 ")
print("## Print ",google.auth.default())

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
print("## 222222222 ")
# Project ID for this request.
project = 'example' 
# Name of the zone for this request.
zone = 'example
# The name of the managed instance group.
instance_group_manager = 'example-mig'  
print("## 33333333 ")

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    print("## 4444444444 ")
    autoscaler_body = {
      "name": f"{instance_group_manager}",
      "target": f"projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}",
      "autoscalingPolicy": {
          "minNumReplicas": 0,
          "maxNumReplicas": 3,
          "mode": "on"
      }
    
    }

    print(autoscaler_body)
    request = service.autoscalers().update(project=project, zone=zone, body=autoscaler_body)
    response = request.execute()
    print("## 666666666 ")
    pprint(response)



    print("Autoscaling On Success!\n")
    return 200

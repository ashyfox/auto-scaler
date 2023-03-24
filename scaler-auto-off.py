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


credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
# Project ID for this request.
project = 'example' 
# Name of the zone for this request.
zone = 'example'
# The name of the managed instance group.
instance_group_manager = 'example-mig'  
# The number of running instances that the managed instance group should maintain at any given time.
# The group automatically adds or removes instances to maintain the number of instances specified by
# this parameter.
size = 0  


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    request = service.autoscalers().get(project=project, zone=zone, autoscaler=instance_group_manager)
    response = request.execute()

    print("Get Instance group :\n",response)
    print("Response status : ",response['autoscalingPolicy']['mode'])
    if response['autoscalingPolicy']['mode'] == 'ON' :
        autoscaler_body = {
            "name": f"{instance_group_manager}",
            "target": f"projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}",
            "autoscalingPolicy": {
                "minNumReplicas": 0,
                "maxNumReplicas": 3,
                "mode": "OFF"
            }
        }

        print(autoscaler_body)
        request = service.autoscalers().update(project=project, zone=zone, body=autoscaler_body)
        response = request.execute()
        pprint(response)
        print("### Autoscaling Off Success!\n")
        request = service.instanceGroupManagers().resize(project=project, zone=zone, instanceGroupManager=instance_group_manager, size=size)
        response = request.execute()
        pprint(response)
        print("### Instance resize Success!\n")
    elif response['autoscalingPolicy']['mode'] == 'OFF':
        print("## Already on")

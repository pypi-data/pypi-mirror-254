import unittest
import boto3
from moto import mock_aws
from aws_common import route53
import datetime


class TestRoute53Case(unittest.TestCase):

    dns = 'example.co.uk'
    current_ip = '88.88.88.88'
    ip = '77.77.77.77'
    
    def get_timestamp(self):
        ct = datetime.datetime.now()
        return str(int(ct.timestamp()))

    @mock_aws
    def test_get_zone_id(self):
        conn = boto3.client('route53', region_name='eu-west-2')
        response = conn.create_hosted_zone(Name=self.dns,CallerReference=self.get_timestamp())
        zone_id = route53.get_route53_zone_id(self.dns)
        assert(response['HostedZone']['Id'] == zone_id)

    @mock_aws
    def test_update_route53_recordset(self):
        conn = boto3.client('route53', region_name='eu-west-2')
        response = conn.create_hosted_zone(Name=self.dns,CallerReference=self.get_timestamp())
        hosted_zone_id = response['HostedZone']['Id']
        # Set to a known value
        response = conn.change_resource_record_sets(
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': self.dns,
                        'ResourceRecords': [
                            {
                                'Value': self.current_ip
                            },
                        ],
                        'TTL': 60,
                        'Type': 'A'
                    },
                }
            ],
        },
        HostedZoneId=hosted_zone_id
        )
        # Set to another value 
        route53.update_route53_record_set(hosted_zone_id, self.dns, self.dns)
        # Read back the value to make sure the change has been made
        response = conn.list_resource_record_sets(HostedZoneId=hosted_zone_id)
        assert({'Value':self.dns} in response['ResourceRecordSets'][0]['ResourceRecords'])

    def setUp(self):
        assert(True)

    def tearDown(self):
        assert(True)
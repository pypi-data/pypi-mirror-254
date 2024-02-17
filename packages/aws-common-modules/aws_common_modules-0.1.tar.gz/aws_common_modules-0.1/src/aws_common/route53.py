import boto3

def get_route53_zone_id(domain_name):
    client = boto3.client('route53')
    response = client.list_hosted_zones()
    for zone in response['HostedZones']:
        if zone['Name'].rstrip('.') == domain_name:
            return zone['Id']

def update_route53_record_set(zone_id, record_set_id, ip_address):
    client = boto3.client('route53')
    response = client.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': record_set_id,
                        'Type': 'A',
                        'TTL': 60,
                        'ResourceRecords': [
                            {
                                'Value': ip_address
                            },
                        ],
                    }
                },
            ]
        }
    )
    return response['ChangeInfo']['Id']
## Introduction
A python module which wraps boto3 functions to provide commonly used AWS operations.

### Example Usage
### Service: Route53
```
#get the aws zone_id, given the domain name, e.g example.com
zone_id = route53.get_route53_zone_id(domain_name)
```
```
#update dns record with new ip
route53.update_route53_record_set(zone_id, domain_name, ip)
```

### Building 
```
hatch build -t wheel
twine upload --repository testpypi dist/*
```

### Running tests
```
cd src
python -m unittest test/test_route53.py
```
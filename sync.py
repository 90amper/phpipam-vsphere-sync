import config
import json
# from phpipam_client import PhpIpamClient, GET, PATCH

""" ipam = PhpIpamClient(
    username=config.ipamConf["username"],
    password=config.ipamConf["password"],
    url=config.ipamConf["url"],
    app_id=config.ipamConf["app_id"],
    token=config.ipamConf["token"],
    encryption=config.ipamConf["encryption"]
) """
import phpipam_api

ipam = phpipam_api.PhpipamAPI(
    api_url=config.ipamConf["url"],
    app_id=config.ipamConf["app_id"],
    api_user=config.ipamConf["username"],
    api_password=config.ipamConf["password"]
    )

def jp (jsonData):
    print(json.dumps(jsonData,indent=2,))

# read object
jp(ipam.sections.get())
jp(ipam.subnets.getAddresses(subnet_id=7))

""" ipam.get('/sections/', {
    'filter_by': 'id',
    'filter_value': 2,
}) """

""" # create object
ipam.post('/sections/', {
    'description': 'example',
})

# update object
ipam.patch('/sections/1/', {
    'description': 'example',
})

# delete object
ipam.delete('/sections/1/')

# read object
ipam.query('/sections/', method=GET)

# update object
ipam.query('/sections/1/', method=PATCH, data={
    'description': 'example',
}) """
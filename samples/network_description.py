from orionsdk import SwisClient
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = ""
password = ""
server = ""
network_address = "x.x.x.x"
device_name = ""

def change_network_description(network_address, device_name):
    """Change the description of a network"""
    swis = SwisClient(server, username, password, verify=False)
    query = f"""SELECT TOP 1 uri, SubnetId, ParentId, Address, AddressMask, CIDR, FriendlyName, Comments
                FROM IPAM.Subnet WHERE Address='{network_address}'
                """
    query_results = swis.query(query)
    uri = query_results["results"][0]["uri"]
    results = swis.update(uri, Comments=device_name)
    
    print(results)
    return results

# change_network_description(network_address=network_address, device_name=device_name)

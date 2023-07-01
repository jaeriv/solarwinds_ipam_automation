from orionsdk import SwisClient
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = ""
password = ""
server = ""
ip_address = "x.x.x.x"
device_name = ""

def change_dns_backward(ip_address, device_name):
    """Change the DNSBackward name of an IP address"""
    swis = SwisClient(server, username, password, verify=False)
    query = f"""SELECT TOP 1 uri, IpNodeId, SubnetId, IPOrdinal, IPAddress, IPMapped, DnsBackward, Status
                FROM IPAM.IPNode WHERE IPAddress='{ip_address}'
                """
    query_results = swis.query(query)
    uri = query_results["results"][0]["uri"]
    results = swis.update(uri, DnsBackward=device_name)
    
    print(results)
    return results

# change_dns_backward(ip_address=ip_address, device_name=device_name)

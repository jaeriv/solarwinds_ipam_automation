from orionsdk import SwisClient
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = ""
password = ""
server = ""
ip_address = "x.x.x.x"

def change_status(ip_address):
    """
    Change status of IP in SolarWinds IPAM
    1 = Used
    2 = Available
    4 = Reserved 
    """
    swis = SwisClient(server, username, password, verify=False)
    results = swis.invoke(
        "IPAM.SubnetManagement",
        "ChangeIpStatus",
        ip_address,
        2 # Status Code
    )
    print(results)
    return results

# change_status(ip_address=ip_address)

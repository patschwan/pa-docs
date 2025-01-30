import os
from dotenv import load_dotenv
from TM1py.Services import TM1Service

# envs for connection
load_dotenv()
user = os.getenv('ADM_USER')
pw = os.getenv('ADM_PW')
namespace = os.getenv('CAM')
address = os.getenv('TM1HOST')
gateway = os.getenv('CAMURI')
port = os.getenv('HTTP')
ssl = os.getenv('SSL')

## Example interactive Auth
# user = input("TM1 User (leave empty if SSO): ")
# password = getpass.getpass("Password (leave empty if SSO): ")
user = user
password = pw
namespace = namespace
address = address
gateway = gateway
port = port
ssl = ssl

def test_connect():
    """Test Connection to TM1 Server -> will print server name to console"""

    print("let's go!")

    try:
        with TM1Service(
                address=address,
                port=port,
                user=user,
                password=password,
                namespace=namespace,
                gateway=gateway,
                ssl=ssl) as tm1:
            server_name = tm1.server.get_server_name()
            print("Connection to TM1 established!! your Servername is: {}".format(server_name))
    except Exception as e:
        print("\nERROR:")
        print("\t" + str(e))

    return server_name
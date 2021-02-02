from netmiko import Netmiko
from getpass import getpass

device1_config = {
    "device_type": "cisco_ios",
    "ip": "192.168.2.49",
    "username": "tim",
    "password": "test",
    "secret": "password"


}
device2_config = {
    "device_type": "cisco_ios",
    "ip": "192.168.2.48",
    "username": "tim",
    "password": "test",
    "secret": "password"
}
def show_arp(device):
    net_conn = Netmiko(**device)

    print("This is for the device", device['ip'])
    output = net_conn.send_command("show arp")
    print(output)

def show_ip_int_brief(device):
    net_conn = Netmiko(**device)

    print("This is for the device", device['ip'])
    output = net_conn.send_command("show ip int brief")
    print(output)

def main():
    routers = []
    routers.append(device1_config)
    routers.append(device2_config)

    for rtr in routers:
        show_arp(rtr)
        show_ip_int_brief(rtr)



if __name__ == "__main__":
    main()
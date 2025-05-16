import requests
import json
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class NXOSManager:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{self.host}"
        self.session = requests.Session()
        self.session.verify = False
        self.login()

    def login(self):
        url = f"{self.base_url}/api/aaaLogin.json"
        payload = {
            "aaaUser": {
                "attributes": {
                    "name": self.username,
                    "pwd": self.password
                }
            }
        }
        response = self.session.post(url, json=payload)
        response.raise_for_status()

    def get_snmp(self):
        url = f"{self.base_url}/api/node/mo/sys/snmp.xml?query-target=subtree"
        response = self.session.get(url)
        response.raise_for_status()
        return response.text

    def configure_snmp(self):
        url = f"{self.base_url}/api/node/mo/sys.xml"
        payload = """
        <topSystem>
        <snmpEntity>
        <snmpInst>
        <snmpCommSecP commAcess="unspecified" grpName="network-operator" name="NXAPI2">
        <snmpAcl useAclName="gnoc_ro" useIpv4AclName="" useIpv6AclName=""/>
        </snmpCommSecP>
        <snmpTraps>
        <snmpTfeaturecontrol>
        <snmpFeatureOpStatusChange trapstatus="enable"/>
        </snmpTfeaturecontrol>
        <snmpTstpx>
        <snmpLoopInconsistency trapstatus="enable"/>
        <snmpInconsistency trapstatus="enable"/>
        <snmpRootInconsistency trapstatus="enable"/>
        </snmpTstpx>
        <snmpTsysmgr>
        <snmpCseFailSwCoreNotifyExtended trapstatus="enable"/>
        </snmpTsysmgr>
        <snmpTlink>
        <snmpCiscoXcvrMonStatusChange trapstatus="enable"/>
        </snmpTlink>
        <snmpTbridge>
        <snmpNewRoot trapstatus="enable"/>
        <snmpTopologyChange trapstatus="enable"/>
        </snmpTbridge>
        <snmpTconfig>
        <snmpCLIRunningConfigChange trapstatus="enable"/>
        </snmpTconfig>
        </snmpTraps>
        <snmpHost commName="NXAPI2" hostName="192.168.0.101" notifType="traps" secLevel="unspecified" udpPortID="162" version="v2c"/>
        <snmpHost commName="NXAPI2" hostName="192.168.0.102" notifType="traps" secLevel="unspecified" udpPortID="162" version="v2c"/>
        </snmpInst>
        </snmpEntity>
        <datetimeClkPol>
        <datetimeNtpSrcIf srcIf="mgmt0"/>
        <datetimeNtpProvider name="NXAPITIME" preferred="yes" provT="server"/>
        <datetimeNtpProvider name="NXAPITIME2" provT="server"/>
        </datetimeClkPol>
        <aclEntity>
        <ipv4aclAF>
        <ipv4aclACL name="gnoc_ro">
        <ipv4aclACE action="permit" dstPrefix="0.0.0.0" protocol="ip" seqNum="60" srcPrefix="192.168.0.101" srcPrefixLength="32" userSetBit="1"/>
        <ipv4aclACE action="permit" dstPrefix="0.0.0.0" protocol="ip" seqNum="50" srcPrefix="192.168.0.101" srcPrefixLength="32" userSetBit="1"/>
        <ipv4aclACE action="permit" dstPrefix="0.0.0.0" protocol="ip" seqNum="30" srcPrefix="192.168.0.101" srcPrefixLength="32" userSetBit="1"/>
        <ipv4aclACE action="permit" dstPrefix="0.0.0.0" protocol="ip" seqNum="10" srcPrefix="192.168.0.101" srcPrefixLength="24" userSetBit="1"/>
        <ipv4aclACE action="permit" dstPrefix="0.0.0.0" protocol="ip" seqNum="20" srcPrefix="192.168.0.101" srcPrefixLength="26" userSetBit="1"/>
        <ipv4aclACE action="permit" dstPrefix="0.0.0.0" protocol="ip" seqNum="40" srcPrefix="192.168.0.101" srcPrefixLength="32" userSetBit="1"/>
        </ipv4aclACL>
        </ipv4aclAF>
        </aclEntity>
        <syslogSyslog>
        <syslogRemoteDest host="192.168.0.101" severity="information" vrfName="default"/>
        </syslogSyslog>
        </topSystem>
        """
        response = self.session.post(url, data=payload)
        response.raise_for_status()
        return response.text

    def get_interface_eth1_11(self):
        url = f"{self.base_url}/api/node/mo/sys/intf/phys-[eth1/11].json"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def configure_interface_eth1_11(self):
        url = f"{self.base_url}/api/node/mo/sys/intf/phys-[eth1/11].json"
        payload = {
            "l1PhysIf": {
                "attributes": {
                    "descr": "Configured with NX-API REST"
                }
            }
        }
        response = self.session.put(url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_vlans(self):
        url = f"{self.base_url}/api/node/class/l2BD.json?query-target-filter=and(ne(l2BD.id,\"1\"))"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_vlan_1(self):
        url = f"{self.base_url}/api/node/mo/sys/bd/bd-[vlan-1].json"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_vlan_501(self):
        url = f"{self.base_url}/api/node/mo/sys/bd/bd-[vlan-501].json"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def create_vlan_501(self):
        url = f"{self.base_url}/api/node/mo/sys/bd/bd-[vlan-501].json"
        payload = {
            "l2BD": {
                "attributes": {
                    "fabEncap": "vlan-501",
                    "name": "NX-API-REST1"
                }
            }
        }
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_vlan_501(self):
        url = f"{self.base_url}/api/node/mo/sys/bd/bd-[vlan-501].json"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.text

    def get_full_object_tree(self):
        url = f"{self.base_url}/api/node/mo/sys.json?query-target=subtree"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

def main():
    host = "sbx-nxos-mgmt.cisco.com"
    username = "admin"
    password = "Admin_1234!"

    nxos = NXOSManager(host, username, password)

    while True:
        print("\nCisco NX-OS NX-API REST Interface Menu:")
        print("1. Get SNMP Configuration")
        print("2. Configure SNMP")
        print("3. Get Interface Eth1/11 Configuration")
        print("4. Configure Interface Eth1/11")
        print("5. Get VLANs")
        print("6. Get VLAN 1")
        print("7. Get VLAN 501")
        print("8. Create VLAN 501")
        print("9. Delete VLAN 501")
        print("10. Get Full Object Tree")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(nxos.get_snmp())
        elif choice == "2":
            print(nxos.configure_snmp())
        elif choice == "3":
            print(json.dumps(nxos.get_interface_eth1_11(), indent=2))
        elif choice == "4":
            print(json.dumps(nxos.configure_interface_eth1_11(), indent=2))
        elif choice == "5":
            print(json.dumps(nxos.get_vlans(), indent=2))
        elif choice == "6":
            print(json.dumps(nxos.get_vlan_1(), indent=2))
        elif choice == "7":
            print(json.dumps(nxos.get_vlan_501(), indent=2))
        elif choice == "8":
            print(json.dumps(nxos.create_vlan_501(), indent=2))
        elif choice == "9":
            print(nxos.delete_vlan_501())
        elif choice == "10":
            print(json.dumps(nxos.get_full_object_tree(), indent=2))
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
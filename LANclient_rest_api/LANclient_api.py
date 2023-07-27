from logging import raiseExceptions
from types import new_class
import requests
from . import LANclient_Blueprint
from flask import jsonify, request
import json
import time
import datetime
import telnetlib
import paramiko

htmlLog = []


@LANclient_Blueprint.route('/LANclient/ping')
def LANclient_ping():
    return "Pinged-- LANclient"

#
# def send_req(topic_name, API_ENDPOINT, message, htmlLog=None):
#     if (type(message) is str):
#         data = {"topicName": topic_name, "message": message}
#     elif (type(message) is list):
#         data = {"topicName": topic_name, "message": '\n'.join(str(v) for v in message)}
#     if htmlLog != None:
#         htmlLog.append(message)
#     try:
#         requests.post(url='http://127.0.0.1:4000/execution/live-logs', json=data,
#                       headers={'Content-type': 'application/json'})
#     except Exception as ex:
#         print(ex)
#
#
# def check_len(v6_addr):
#     request_json = {}
#     response_json = {}
#     htmlLog = []
#     request_json = request.json
#     for i in v6_addr:
#         if i.startswith("2001") and len(v6_addr) == 2:
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Success It has both the address',
#                      htmlLog)
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = "Success It has both the address"
#     else:
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                  'Failure !. It does not have both the address', htmlLog)
#         response_json["RESULT"] = "0"
#         response_json["FailureReason"] = "Success It does not have both the address"
#
#
# @LANclient_Blueprint.route('/LANclient/get_vlan', methods=['POST'])
# @LANclient_Blueprint.route('/LANclient/get_vlan_info', methods=['POST'])
# def get_vlan():
#     request_json = {}
#     response_json = {}
#     htmlLog = []
#     request_json = request.json
#     # send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Launching VLAN API', htmlLog)
#     try:
#
#         vmIp = request_json['vm_ip']
#         userName = request_json['username']
#         Password = request_json['password']
#         Req_info = request_json['req_info']
#         # send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Trying to get the vlan Addresses', htmlLog)
#         client = paramiko.client.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(vmIp, username=userName, password=Password)
#         _stdin, stdout, _stderr = client.exec_command("ifconfig")
#         data = stdout.read().decode()
#         if "ens224." not in data:
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = "device not connected"
#
#         else:
#             print("outside")
#             v6_addr = []
#             a = data.split("\n")
#             b = list(filter(lambda x: x.startswith("ens224."), a))
#             c = b[0].split(":")
#             d = c[0].split(".")
#             if Req_info == 'Vlan_id':
#                 val = d[1]
#             else:
#                 ipv6addr = list(filter(lambda x: x.endswith("scopeid 0x0<global>"), a))
#                 first_val = ipv6addr[0].split()
#                 second_val = ipv6addr[1].split()
#                 v6_addr.append(first_val[1])
#                 v6_addr.append(second_val[1])
#                 check_len(v6_addr)
#                 val = v6_addr
#                 print(first_val[1], second_val[1])
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = val
#         client.close()
#
#     except Exception as ex:
#         print("Exception Occured", ex)
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         response_json["FailureReason"] = message
#         response_json["RESULT"] = "1"
#         response_json["log"] = htmlLog
#     return json.dumps(response_json)
#
#
# def get_exist_vlan(vmIp, userName, Password, Req_info):
#     request_json = {}
#     response_json = {}
#     htmlLog = []
#     try:
#
#         client = paramiko.client.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(vmIp, username=userName, password=Password)
#         _stdin, stdout, _stderr = client.exec_command("ifconfig")
#         data = stdout.read().decode()
#         if "ens224." not in data:
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = "device not connected"
#
#         else:
#             print("outside")
#             v6_addr = []
#             a = data.split("\n")
#             b = list(filter(lambda x: x.startswith("ens224."), a))
#             c = b[0].split(":")
#             d = c[0].split(".")
#             if Req_info == 'Vlan_id':
#                 val = d[1]
#             else:
#                 ipv6addr = list(filter(lambda x: x.endswith("scopeid 0x0<global>"), a))
#                 first_val = ipv6addr[0].split()
#                 second_val = ipv6addr[1].split()
#                 v6_addr.append(first_val[1])
#                 v6_addr.append(second_val[1])
#                 check_len(v6_addr)
#                 val = v6_addr
#                 print(first_val[1], second_val[1])
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = val
#         client.close()
#
#     except Exception as ex:
#         print("Exception Occured", ex)
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         response_json["FailureReason"] = message
#         response_json["RESULT"] = "1"
#         response_json["log"] = htmlLog
#     return json.dumps(response_json)
#
#
# @LANclient_Blueprint.route('/LANclient/connect client', methods=['POST'])
# def connect():
#     request_json = {}
#     response_json = {}
#     htmlLog = []
#     request_json = request.json
#     print(request_json)
#     try:
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Trying to get exist VLAN id', htmlLog)
#         vmIp = request_json['vm_ip']
#         userName = request_json['username']
#         Password = request_json['password']
#         new_vlan = request_json['vlan']
#         Req_info = 'Vlan_id'
#         response = get_exist_vlan(vmIp, userName, Password, Req_info)
#         print("Get exist vlan response ====>", response, type(response), json.loads(response),
#               type(json.loads(response)))
#         exist_vlan = json.loads(response)["returnValue"]
#         # exist_vlan='1247'
#         print("It Worked ")
#         if 'Bridge' in request_json['scenarioName'] or 'bridge' in request_json['scenarioName']:
#             print("Waiting additionally Before Connecting to VM")
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                      'Waiting additionally Before Connecting to VM ' + exist_vlan, htmlLog)
#             time.sleep(300)
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Connected VLAN ' + exist_vlan, htmlLog)
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Checking if it is already connected VLAN',
#                  htmlLog)
#         if exist_vlan == new_vlan:
#             client = paramiko.client.SSHClient()
#             client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             client.connect(vmIp, username=userName, password=Password)
#             _stdin, stdout, _stderr = client.exec_command("sudo dhclient -4 -v ens224." + exist_vlan)
#             data = stdout.read().decode()
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'], "DHCP configuration is working properly",
#                      htmlLog)
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = "Requested device is already connected , Response from vm : " + data
#         elif exist_vlan == "device not connected":
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Doesnot have any connection', htmlLog)
#             client = paramiko.client.SSHClient()
#             client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             client.connect(vmIp, username=userName, password=Password)
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                      'Adding new device with ens.224 Interface', htmlLog)
#             _stdin, stdout, _stderr = client.exec_command("./VlanOp.sh " + new_vlan + " add")
#             data = stdout.read().decode()
#             print("data")
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = data
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                      'New device connected with ens224.' + new_vlan, htmlLog)
#             client.close()
#         else:
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Connected device doesnt match', htmlLog)
#             client = paramiko.client.SSHClient()
#             client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             client.connect(vmIp, username=userName, password=Password)
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                      'Delete existing device with ens224.' + exist_vlan, htmlLog)
#             _stdin, stdout, _stderr = client.exec_command("./VlanOp.sh " + exist_vlan + " delete")
#             time.sleep(2)
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                      'New device connected with ens224.' + new_vlan, htmlLog)
#             _stdin, stdout, _stderr = client.exec_command("./VlanOp.sh " + new_vlan + " add")
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'], "DHCP configuration is working properly",
#                      htmlLog)
#             data = stdout.read().decode()
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = data
#             # send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'New device connected with ens224.'+new_vlan, htmlLog)
#             client.close()
#
#     except Exception as ex:
#         print("Exception Occured", ex)
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         response_json["FailureReason"] = message
#         response_json["RESULT"] = "1"
#         response_json["log"] = htmlLog
#     time.sleep(30)
#     return json.dumps(response_json)
#
#
# @LANclient_Blueprint.route('/LANclient/connect_viaDHCP', methods=['POST'])
# def connect_viaDHCP():
#     request_json = {}
#     response_json = {}
#     htmlLog = []
#     request_json = request.json
#     print(request_json)
#     try:
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Trying to get exist VLAN id', htmlLog)
#         vmIp = request_json['vm_ip']
#         userName = request_json['username']
#         Password = request_json['password']
#
#         Req_info = 'Vlan_id'
#         response = get_exist_vlan(vmIp, userName, Password, Req_info)
#         print("Get exist vlan response ====>", response, type(response), json.loads(response),
#               type(json.loads(response)))
#         exist_vlan = json.loads(response)["returnValue"]
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Connected VLAN ' + exist_vlan, htmlLog)
#
#         client = paramiko.client.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(vmIp, username=userName, password=Password)
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                  'Command Executed : sudo dhclient -4 -v ens224.' + exist_vlan, htmlLog)
#         _stdin, stdout, _stderr = client.exec_command("sudo dhclient -4 -v ens224." + exist_vlan)
#         data = stdout.read().decode()
#         response_json["RESULT"] = "0"
#         response_json["returnValue"] = data
#         client.close()
#
#
#     except Exception as ex:
#         print("Exception Occured", ex)
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         response_json["FailureReason"] = message
#         response_json["RESULT"] = "1"
#         response_json["log"] = htmlLog
#     time.sleep(30)
#     return json.dumps(response_json)
#
#
# @LANclient_Blueprint.route('/LANclient/exec_cmd_vm', methods=['POST'])
# def exec_cmd_vm():
#     request_json = {}
#     response_json = {}
#     htmlLog = []
#     request_json = request.json
#     print(request_json)
#     try:
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Trying to get exist VLAN id', htmlLog)
#         vmIp = request_json['vm_ip']
#         userName = request_json['username']
#         Password = request_json['password']
#         ip = request_json['ip_address']
#         payload = json.dumps({
#             "topicName": "",
#             "API_ENDPOINT": "",
#             "vm_ip": vmIp,
#             "username": userName,
#             "password": Password,
#             "req_info": "Vlan_id"
#         })
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         response = requests.request("POST", "http://127.0.0.1:5001/LANclient/get_vlan", headers=headers, data=payload)
#         print(response)
#         exist_vlan = json.loads(response.text)["returnValue"]
#         client = paramiko.client.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(vmIp, username=userName, password=Password)
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                  'Command Executed : sudo dhclient -4 -v ens224.' + exist_vlan, htmlLog)
#         _stdin, stdout, _stderr = client.exec_command("wget http://" + ip)
#         data = stdout.read().decode()
#         response_json["RESULT"] = "0"
#         response_json["returnValue"] = data
#         client.close()
#
#     except Exception as ex:
#         print("Exception Occured", ex)
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         response_json["FailureReason"] = message
#         response_json["RESULT"] = "1"
#         response_json["log"] = htmlLog
#     time.sleep(30)
#     return json.dumps(response_json)
#
#
# @LANclient_Blueprint.route('/LANclient/ping_from_LAN_client', methods=['POST'])
# @LANclient_Blueprint.route('/LANclient/ping_from_LAN_client_retval', methods=['POST'])
# def Ping_from_lan():
#     request_json = {}
#     response_json = {}
#     htmlLog = []
#     request_json = request.json
#     # send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Launching VLAN API', htmlLog)
#     try:
#
#         vmIp = request_json['vm_ip']
#         iP = request_json['ip']
#         userName = request_json['username']
#         Password = request_json['password']
#         Req_info = request_json['ip format']
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Trying to connect LAN client', htmlLog)
#         client = paramiko.client.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(vmIp, username=userName, password=Password)
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Connected', htmlLog)
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Running ping command', htmlLog)
#         if Req_info == "IPV4":
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                      'Command to be Executed : ping -c 4 ' + iP, htmlLog)
#             _stdin, stdout, _stderr = client.exec_command("ping -c 4 " + iP)
#             data = stdout.read().decode()
#         elif Req_info == "IPV6":
#             vlan = get_exist_vlan(vmIp, userName, Password, 'Vlan_id')
#             _stdin, stdout, _stderr = client.exec_command("ping6 -c 4 " + iP + "%" + vlan)
#             data = stdout.read().decode()
#         elif Req_info == "LANIPV6":
#             send_req(request_json['topicName'], request_json['API_ENDPOINT'],
#                      'Command to be Executed : ping6 -c 4' + iP, htmlLog)
#             vlan = get_exist_vlan(vmIp, userName, Password, 'Vlan_id')
#             _stdin, stdout, _stderr = client.exec_command("ping6 -c 4 " + iP)
#             data = stdout.read().decode()
#         else:
#             response_json["RESULT"] = "1"
#             response_json["FailureReason"] = "Not a valid IP format"
#         a = data.split("ping")
#         b = list(filter(lambda x: x.startswith(" statistics"), a))
#         c = b[0].split(",")
#         d = c[0].split("---")
#         transmit = d[1]
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Total byte transmit ' + transmit, htmlLog)
#         receive = c[1]
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Total byte receive ' + receive, htmlLog)
#         packet_loss = c[2]
#         send_req(request_json['topicName'], request_json['API_ENDPOINT'], 'Packet loss ' + packet_loss, htmlLog)
#         k = packet_loss.split(" ")
#         if k[1] == "0%":
#             response_json["RESULT"] = "0"
#             response_json["returnValue"] = "pinged sucessfully"
#         elif k[1] == "100%":
#             response_json["RESULT"] = "1"
#             response_json["FailureReason"] = k[1] + " complete packet loss"
#         else:
#             response_json["RESULT"] = "1"
#             response_json["FailureReason"] = k[1] + " partially packet loss"
#         client.close()
#
#     except Exception as ex:
#         print("Exception Occured", ex)
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         response_json["FailureReason"] = message
#         response_json["RESULT"] = "1"
#         response_json["log"] = htmlLog
#     return json.dumps(response_json)

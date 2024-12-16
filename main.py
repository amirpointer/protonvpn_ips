import requests
import csv
response_data = requests.get('https://api.protonmail.ch/vpn/logicals')
response_json = response_data.json()

exit_ip_list = []
enter_ip_list = []

for server in response_json['LogicalServers']:
    for server_info in server['Servers']:
        exit_ip = server_info['ExitIP']
        exit_ip_list.append(exit_ip)

for server in response_json['LogicalServers']:
    for server_info in server['Servers']:
        enter_ip = server_info['EntryIP']
        enter_ip_list.append(enter_ip)

with open('protonvpn_exit_ips.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(zip(exit_ip_list))
with open('protonvpn_enter_ips.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(zip(enter_ip_list))

exit_ip_count = len(exit_ip_list)
enter_ip_count = len(enter_ip_list)
print(f"{exit_ip_count} exit IPs exported to protonvpn_exit_ips.csv")
print(f"{enter_ip_count} enter IPs exported to protonvpn_exit_ips.csv")

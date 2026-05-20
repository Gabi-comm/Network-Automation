import json
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

def main():
    #read json file
    try:
        with open('autoAP-temp.json') as file:
            deviceData = json.load(file)
    except FileNotFoundError:
        print("Error: 'autoAP-temp.json' file is missing")
        return
    
    #parse info from json
    aironet = deviceData.get('aironetInfo', {})
    apConfig = deviceData.get('aironetConfig', {})

    # config script for the device
    deviceConfig = [
        f'hostname {apConfig.get("hostname", "AP")}',
        f'dot11 ssid {apConfig.get("ssid", "WIFI")}',
        f'vlan {apConfig.get("vlan", "1")}',
        f'authentication {apConfig.get("authentication", "open")}',
        f'authentication key-management {apConfig.get("key-man", "wpa")}',
        f'wpa-psk ascii {apConfig.get("wifi-pass", "password")}',
        'guest-mode',
        'default Int Dot11Radio 0',
        'default interface gigabitEthernet 0',
        'int dot11radio 0',
        'no shut',
        f'channel {apConfig.get("channel", "1")}',
        f'encryption mode ciphers {apConfig.get("encr-mod", "aes-ccm")}',
        f'encryption vlan {apConfig.get("vlan", "1")} mode ciphers {apConfig.get("encr-mod", "aes-ccm")}',
        f'ssid {apConfig.get("ssid", "WIFI")}',
        'exit',
        f'interface dot11radio 0.{apConfig.get("vlan", "1")}',
        f'encapsulation dot1q {apConfig.get("vlan", "1")} native',
        'bridge-group 1',
        'exit'
    ]

    #to know that the AP is connecting
    print(f"Connecting to AP at {aironet.get('host')}...")
    
    try:
        #connect to the device's CLI
        accessAutoAP = ConnectHandler(**aironet)

        #use enable command to enter privilege exec mode
        accessAutoAP.enable()

        # Push configurations through global configuration mode
        print("Pushing configurations...")
        output = accessAutoAP.send_config_set(deviceConfig)
        #print CLI output on the terminal
        print(output)
        
        #pinging
        target_ip = input("\nEnter the IP address to ping or press Enter to skip: ") #enter ip from phone
        if target_ip:
            print(f"Pinging {target_ip} from the Access Point...")
            ping_output = accessAutoAP.send_command(f"ping {target_ip}")
            print(ping_output)
            output += f"\n\n--- Ping result for {target_ip} ---\n{ping_output}"

        accessAutoAP.disconnect()

        # save output
        with open('show_run_output.txt', 'w') as file:
            file.write(output)
        print("\n File is saved to 'show_run_output.txt'")
    #if it fails, shows the error
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        print(f"Failed to connect to the device\nError details: {e}")

if __name__ == "__main__":
    main()
def main():
    rst_ip = crt.Dialog.Prompt("What is your RST IPv4 Address? ")
    if not rst_ip: 
        return

    lab = crt.Dialog.Prompt(
        "What Lab will you be using? (Input the number)\n"
        "\n1 = RSTvX\n2 = RST Subnet\n3 = RST Hosts (Day 5)\n"
        "4 = RST Mini\n5 = RST Multisite\n6 = MPLS\n7 = WAN\n"
        "8 = 3Tier\n9 = NetAuto\n10 = InterNetwork\n0 = Manual Ports\n"
    )

    #instead of else if, i use dic
    lab_ports = {
        "1": range(2001, 2017),
        "2": range(2001, 2010),
        "3": [2001, 2002] + list(range(2005, 2017)),
        "4": [2001, 2002] + list(range(2005, 2011)) + [2013],
        "5": [2002, 2008, 2010, 2012, 2013, 2015, 2016],
        "6": range(2017, 2029),
        "7": range(2135, 2155),
        "8": list(range(2204, 2218)) + [2339],
        "9": range(2262, 2273),
        "10": range(2801, 2835)
    }

    connections = []

    if lab == "0":
        specify_ports = crt.Dialog.Prompt("Specify port numbers (separated by spaces):\nex. 2001 2002 2003")
        if specify_ports:
            ports = specify_ports.split()
            connections = [f"/TELNET {rst_ip} {port}" for port in ports]
    elif lab in lab_ports:
        connections = [f"/TELNET {rst_ip} {port}" for port in lab_ports[lab]]
    else:
        crt.Dialog.MessageBox("Invalid lab selection or action canceled.")
        return

    # Open the connections in SecureCRT tabs
    crt.Screen.Synchronous = True
    for connection in connections:
        crt.Session.ConnectInTab(connection)
    crt.Screen.Synchronous = False

main()
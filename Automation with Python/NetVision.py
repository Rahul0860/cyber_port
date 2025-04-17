
def vizu(ipdata):

    from rich.console import Console
    from rich.table import Table
    table = Table(title="Pcapng Packet Report",show_lines=True)

    table.add_column("Source IP", justify="right", style="cyan",)
    table.add_column("Src_port", justify="right", style="white")
    table.add_column("Desertion IP", style="magenta")
    table.add_column("Dst_port", justify="right", style="white")
    table.add_column("Freq", justify="right", style="green")
    table.add_column("protocols", justify="right", style="cyan")
    #table.add_column("protocol", justify="right", style="cyan")


    # cecklist = ['eth', 'ip', 'udp', 'dns', 'arp', 'tcp', 'http']
    for i in ipdata:
        protocol = str(i[5:])
        table.add_row(i[0], i[3], i[1], i[4], str(i[2]), protocol)
    console = Console()
    console.print(table)

# -------------------------*Data_Transforming_printing*----------------------------------#
def exandtrn(data1):
    list_ip = []

    for key, value in data1.items():
        output_list = [item for item in key if item != '-']
        for i in range(len(value)):
            output_list.append(value[i])
        #output_list.append(value)
        list_ip.append(output_list)
    sorted_list = sorted(list_ip, key=lambda x: x[2], reverse=True)
    #print(sorted_list)
    vizu(sorted_list)

# -------------------------*main*----------------------------------#
def pandf():
    import pyshark as pys
    tshark_path = r'D:\wirshark_installed\Wireshark\tshark.exe'
    print("fcap_open")
    capture = pys.FileCapture(input_file="fcap.pcapng", display_filter="!(arp)",tshark_path=tshark_path, )  # disable_protocol="arp"

    data1 = {}

    for packet in capture:
        #p_no = packet.number
        if 'ipv6' in packet:
            ips = packet.ipv6.src
            ipd = packet.ipv6.dst
        else:
            ips = packet.ip.src
            ipd = packet.ip.dst
        formated_ip = (ips,'-',ipd)
        #print(formated_ip)

        if formated_ip in data1.keys():
             # Update Values...
             c = data1[formated_ip][0] + 1
             data1[formated_ip][0] = c
        else:
            l1 = [1]
            l2 = []
            for layer in packet.layers:
                l2.append(layer.layer_name)
            if 'tcp' in l2:
                l2.insert(0,(packet.tcp.srcport))
                l2.insert(1,(packet.tcp.dstport))
            elif 'udp' in l2:
                l2.insert(0,packet.udp.srcport)
                l2.insert(1,packet.udp.dstport)
            for i in l2:
                l1.append(i)
            data1[formated_ip] = l1
            l2.clear()

    capture.close()

    exandtrn(data1)
    # for key, value in data1.items():
    #      print(f"ips: {key} |frqs: {value}")
pandf()
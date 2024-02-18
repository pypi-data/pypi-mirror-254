import os
import re
import subprocess
import uuid
import speedtest
from texttable import Texttable


t = Texttable()
systemDetails = os.uname()


def run_command(cmd):
    try:
        stdout = subprocess.check_output(cmd, shell=True)
        return stdout.decode("utf-8"), True
    except Exception as error:
        return error, False


def node_details():
    local_dict = {}
    list_data = ["sysname", "nodename", "release", "version", "machine"]
    for item in list_data:
        try:
            output = getattr(systemDetails, item)
            local_dict[item] = output
        except Exception as err:
            local_dict[item] = str(err)
    return local_dict


def node_current_user():
    current_user, status = run_command("whoami")
    return current_user


def node_mac_address():
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac


def node_all_connected_wifi():
    res = os.listdir("/etc/NetworkManager/system-connections/")
    print(res)
    wifi_dict = {}
    for i in res:
        try:
            out, status = run_command("sudo cat /etc/NetworkManager/system-connections/'{0}' | grep 'psk='".format(i))
            out = (str(out).split("psk="))[1]
            if status:
                wifi_dict[i] = out[:-1]
        except Exception as error:
            print(error)
    return wifi_dict


def node_connected_wifi():
    tmp_dict = {}
    out, status = run_command("iwgetid")

    wifi_connected = str(out).split("ESSID:")[-1]
    wifi_connected = wifi_connected.strip("\n")
    wifi_connected = wifi_connected.replace('"',"") + ".nmconnection"
    res = os.listdir("/etc/NetworkManager/system-connections/")
    for i in res:
        if wifi_connected in i:
            wifi_connected = i
            break
    try:
        out, status = run_command("sudo cat /etc/NetworkManager/system-connections/'{0}' | grep 'psk='".format(wifi_connected))
        out = (str(out).split("psk="))[1]
        if status:
            tmp_dict[wifi_connected] = out
            return tmp_dict
        else:
            tmp_dict[wifi_connected] = "UNKOWN"
            return tmp_dict
    except Exception as error:
        print(error)


def node_open_ports():
    word = ""
    list_words = []
    # out, status = run_command("sudo netstat -tulpn | grep LISTEN")
    out, status = run_command("sudo lsof -i -P -n | grep LISTEN")
    # Distribute in lines
    for data in out:
        if data != "\n":
            word = word + data
        else:
            list_words.append(word)
            word = ""
    # Service Name with port
    new_service_list = []
    for value in list_words:
        service = value.split()[-2]
        service = service.split(":")[-1]
        new_service_list.append(service)
    new_service_list = (list(set(new_service_list)))
    return new_service_list


def node_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000  # Convert to Mbps
    upload_speed = st.upload() / 1000000  # Convert to Mbps
    return download_speed, upload_speed


def node_complete_analysis():
    # Node Details
    details = node_details()
    # current user
    user = node_current_user()
    # mac
    mac= node_mac_address()
    # node_connected_wifi
    current_connected_wifi = node_connected_wifi()
    keys = list(current_connected_wifi.keys())
    values = list(current_connected_wifi.values())

    # spped
    # download, upload = node_speed_test()
    download, upload = 5,5

    # node open
    open_ports = node_open_ports()

    t.add_rows([['Focused Item', 'Data'],
                ['System Name', details["sysname"]],
                ['Architecture', details['machine']],
                ['release', details['release']],
                ['version', details['version']],
                ['IP address', details["nodename"]],
                ["MAC address", mac],
                ['Current User', user],
                ['WIFI : {0}'.format(keys[0]), values[0]],
                ["Download Speed  (Mbps)", download],
                ["Upload Speed (Mbps) ", upload],
                ["Open Service with Ports",open_ports]
                ])
    print(t.draw())
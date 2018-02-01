#!/usr/bin/env python3

def connect(ipaddress, ports):

    print("ip: ", ipaddress)

    print("ports: ", ports)

    ipaddress = '10.10.10.1'

    ports.append(8080)

if __name__=="__main__":

    ipaddress = '192.168.1.1'

    ports = [22,23,24]

    print("before connect:")

    print("ip: ", ipaddress)

    print("ports: ", ports)

    print("in connrct:")

    connect(ipaddress, ports)

    print("after connect:")

    print("ip: ",ipaddress)

    print("ports: ", ports)

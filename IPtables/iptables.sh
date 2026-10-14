#!/bin/bash

iptables -F
iptables -t nat -F

iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

iptables -A INPUT -i lo -j ACCEPT

iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

#iptables -A INPUT -s 192.168.0.1/24 -j ACCEPT
iptables -A INPUT -i enp0s3 -o enp0s8 -j ACCEPT

#iptables -A FORWARD -s 10.0.2.15/24 -d 192.168.0.1/24 -j ACCEPT
iptables -A FORWARD -s enp0s3 -o enp0s8 -j ACCEPT

#iptables -t nat -A POSTROUTING -d 10.0.2.15 -j MASQUERADE
iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE


iptables -A INPUT -i enp0s3 --dport 80 -m state --state NEW -m recent --set --name WEB_HARDEN

iptables -A INPUT -i enp0s3 --dport 80 -m state --state NEW -m recent --update --seconds 10 --hitcount 5 --name WEB_HARDEN -j DROP


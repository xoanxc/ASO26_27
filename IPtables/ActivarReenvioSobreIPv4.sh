sudo sysctl -w net.ipv4.ip forward=1

# Modificar de forma permanente:
# Descomentar la línea 28 "net.ipv4.ip_forward=1" en el fichero /etc/sysctl.conf
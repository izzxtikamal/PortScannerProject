import socket
import common_ports

def get_open_ports(target, port_range, verbose=False):
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        return "Error:Invalid hostname"
    
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        sock.close()

        if result == 0:
            open_ports.append(port)

    if verbose: 
        result_string = f"Open ports for {target} ({ip_address})\n"
        result_string += "PORT         SERVICE\n"
        for port in open_ports:
            service_name = common_ports.services.get(port, "unkown")
            result_string += f"{str(port).ljust(9)}{service_name}\n"
        return result_string
    else:
        return open_ports



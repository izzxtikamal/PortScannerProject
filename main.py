from port_scanner import get_open_ports

result1 = get_open_ports("209.216.230.240", [440, 445])
result2 = get_open_ports("www.stackoverflow.com", [79, 82])
result3 = get_open_ports("scanme.nmap.org", [20, 80], True)


#Print the result
print(result1)

print(result2)

print(result3)
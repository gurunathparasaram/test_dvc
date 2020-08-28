import sys

ip_path = sys.argv[1]
op_path = sys.argv[2]

with open(ip_path) as ip_file, open(op_path, "w") as op_file:
    ip_lines = ip_file.readlines()
    for line in ip_lines:
        op_file.write(line)

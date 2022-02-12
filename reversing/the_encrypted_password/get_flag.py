import re
from pwn import process, context

context.log_level = "warn"
proc = process("echo '' | ltrace -s 100 ./encrypted_password", shell=True)
output = proc.recvall().decode()
password = re.findall(r'strcmp\(.*?,\s"(.*?)"', output)[0]

proc = process(F"echo '{password}' | ./encrypted_password", shell=True)
flag = re.findall(r"247CTF{.*}", proc.recvall().decode())[0]
print(flag)

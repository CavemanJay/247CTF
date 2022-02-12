import re
from pwn import ELF
from itertools import takewhile

offset = 0x00100000
main = 0x0010063a
main_end = 0x0010065f

elf = ELF("the_more_the_merrier")
elf.address += offset

main_func = elf.disasm(main, main_end-main)
flag_location = re.findall(r"lea\s+rax,.*?# (0x[\w\d]+)", main_func)[0]
flag_location = int(flag_location, 16)  

# Get rid of null padding bytes
flag_mem = elf.read(flag_location, 400).replace(b'\00', b'') 

# Read the flag bytes
flag = map(chr, takewhile(lambda x: x != ord('}'), flag_mem))
print("".join(flag)+"}")

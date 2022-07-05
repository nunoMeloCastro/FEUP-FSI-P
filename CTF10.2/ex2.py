#!/usr/bin/python3
from pwn import *

DEBUG = True

if DEBUG:
    r = process('./program')
else:
    r = remote('ctf-fsi.fe.up.pt', 4000)


r.interactive()
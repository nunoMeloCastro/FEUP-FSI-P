# Trabalho realizado na Semana #5

## Task 1
When we run the 32 and 64 bits versions we found no difference in their execution because our system is a 64bits one, so its compatible with both.

## Task 2
We ran the commands given in order to disable the stack guard and compile the program as a root owned SET-UID program and after running the ls command we can verify that the executables are root owned as their are shown with the red highlighting.

![image.png](./image.png)

## Task 3
To launch the attack the first step was to calculate the offset between the buffer starting position and the return address position. For that purpose, we used gdb.

![image-1.png](./image-1.png)

We know that the return address will be stored 4 bytes above the ebp so the offset wiil be 108 + 4 = 112.
The next step was to modify the exploit according to the info acquired.
We started by inserting the shellcode.
```
shellcode= (
  "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
  "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31"
  "\xd2\x31\xc0\xb0\x0b\xcd\x80"  
).encode('latin-1')
```

For the starting postion of the shellcode we decided to put it right at the end of the content.
```
start = 517 - len(shellcode) 
```

For the return address position we figured it wouldn't be same as the one obtained when the program was ran with gdb because gdb pushes additional data onto the stack. For this same reason we determined this address would be deeper in the stack and by trial-error method we found that 0x100 was enough to cover the additional data and get our exploit runnig as intended.
```
ret = 0xffffcac8 + 0x100
```

Last but not least we needed to change the offset value  to the one which was calculated previously
```
offset = 112 
```

![image-2.png](./image-2.png)

Last step was to run the exploit and then the stack-L1 executable and verify if we got a shell running.

![image-3.png](./image-3.png)

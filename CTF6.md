# CTF realizado na Semana #6

## Desafio 1

### Qual é a linha do código onde a vulnerabilidade se encontra?
There is a vulnerability in line 27 of the main.c file.

![image-21.png](./image-21.png)

### O que é que a vulnerabilidade permite fazer?
This vulnerability lets us read or write memory or execute harmful code. In this case we want to read the content of a file, the flag.

### Qual é a funcionalidade que te permite obter a flag?
We may use, for example "%s", "%x" or "%n", format specifiers to print or write data from the stack or others locations.

### Ataque

Knowing the flag is stored in a global variable, we are able to locate its memory address through gdb debugger.

![image-20.png](./image-20.png)

Using a trial-error method we managed to find out the we needed only one "%x" to print the first 4 bytes of our input.
In the beginning of the input we inserted "!!!!" which is equivalent to 0x21212121. With this we were able to easily locate the memory address on the stack the we could manipulate.

![image-22.png](./image-22.png)

With this information, we configured our exploit to provide the flag's memory address in the first four bytes followed by "%s" to print its content.

![image-23.png](./image-23.png)

![image-24.png](./image-24.png)

## Desafio 2

### Qual é a linha do código onde a vulnerabilidade se encontra? E o que é que a vulnerabilidade permite fazer?
There is a vulnerability in line 14 of the main.c file.

![image-25.png](./image-25.png)

### A flag é carregada para memória? Ou existe alguma funcionalidade que podemos utilizar para ter acesso à mesma.
This time we don't have the flag loaded into memory but have a key which is used in a comparison to open a reverse shell. 

![image-30.png](./image-30.png)

With gdb we can attach into the running proccess and retrieve the key's memory address. 

![image-26.png](./image-26.png)

### Para desbloqueares essa funcionalidade o que é que tens de fazer?
We need to change the key value to 0xBEEF with the "%n" format specifier in order to verify this condition and gain remote access.

![image-29.png](./image-29.png)

### Ataque
The process was similar to the one in the previous challenge but we ran into a problem. As our buffer printed right in the first position we needed to find a way to provide enough characters so we could change the key value to 0xBEEF (48879 decimal).
We overcame this problem by inserting a dummy address before the key one and printing the content with the number of characters needed to fulfill the correct change of the key. ( 48879-(4+4) = 48871 ) 
With this we were able to gain remote access to host machine and its files.

![image-27.png](./image-27.png)

![image-28.png](./image-28.png)







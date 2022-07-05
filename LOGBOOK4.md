# Trabalho realizado na Semana #4

## Task 1

In this first task we experimented with the commands shown in the lab guide and obtained:

```
[11/17/21]seed@VM:~/.../Labsetup$ printenv SHELL/bin/bash
[11/17/21]seed@VM:~/.../Labsetup$ 
[11/17/21]seed@VM:~/.../Labsetup$ env | grep PWD
PWD=/home/seed/seed-labs/category-software/Environment_Variable_and_SetUID/Labsetup
OLDPWD=/home/seed/seed-labs/category-software/Environment_Variable_and_SetUID 
```
```
[11/17/21]seed@VM:~/.../Labsetup$ TEMPORARY_VAR='test'
[11/17/21]seed@VM:~/.../Labsetup$ export TEMPORARY_VAR
[11/17/21]seed@VM:~/.../Labsetup$ printenv TEMPORARY_VAR
test
[11/17/21]seed@VM:~/.../Labsetup$ unset TEMPORARY_VAR
[11/17/21]seed@VM:~/.../Labsetup$ printenv TEMPORARY_VAR
```

## Task 2

After running the program printing the environment variables with the child process and the parent process
we can conclude that there is no change, which means that the child process inherits the environment table 
from its parent process.

```
[11/17/21]seed@VM:~/.../Labsetup$ nano myprintenv.c 
[11/17/21]seed@VM:~/.../Labsetup$ gcc myprintenv.c 
[11/17/21]seed@VM:~/.../Labsetup$ a.out > child
[11/17/21]seed@VM:~/.../Labsetup$ nano myprintenv.c 
[11/17/21]seed@VM:~/.../Labsetup$ gcc myprintenv.c 
[11/17/21]seed@VM:~/.../Labsetup$ a.out > parent
[11/17/21]seed@VM:~/.../Labsetup$ diff child parent
[11/17/21]seed@VM:~/.../Labsetup$
```


## Task 3

>Step 1

When we invoked execve() for the first time no environment variables were shown.

```
[11/17/21]seed@VM:~/.../Labsetup$ nano myenv.c 
[11/17/21]seed@VM:~/.../Labsetup$ gcc myenv.c
[11/17/21]seed@VM:~/.../Labsetup$ a.out > myenv_NULL
[11/17/21]seed@VM:~/.../Labsetup$ cat myenv_NULL | wc -l
0
```

>Step 2

This time there were environment variables.

```
[11/17/21]seed@VM:~/.../Labsetup$ nano myenv.c
[11/17/21]seed@VM:~/.../Labsetup$ gcc myenv.c
[11/17/21]seed@VM:~/.../Labsetup$ a.out > myenv_environ
[11/17/21]seed@VM:~/.../Labsetup$ cat myenv_environ | wc -l
51
```

>Step 3 

When invoking execve() by default no environment variables are inherinted from the calling process to the new program
In order for the process to inherit the environment variables we need to pass them as an argument.

## Task 4

We can conclude that when invoking system(), the environment variables are inherited by default.

```
[11/17/21]seed@VM:~/.../Labsetup$ nano system_call.c
[11/17/21]seed@VM:~/.../Labsetup$ gcc system_call.c 
[11/17/21]seed@VM:~/.../Labsetup$ a.out > file4
[11/17/21]seed@VM:~/.../Labsetup$ cat file4 | wc -l
49
[11/17/21]seed@VM:~/.../Labsetup$ env > file5
[11/17/21]seed@VM:~/.../Labsetup$ cat file5 | wc -l
49
```

## Task 5

After compiling an running this Set-UID program we found out that only the LD_LIBRARY_ PATH wasn't inherinted.
We did some research on the matter and found out that on AIX and Linux the OS has a security feature. 
All programs that contain Set-UID bit won't inherit the LIBPATH or LD_LIBRARY_PATH environment variables.

```
[11/17/21]seed@VM:~/.../Labsetup$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
[11/17/21]seed@VM:~/.../Labsetup$ env | grep LD_LIBRARY_PATH
LD_LIBRARY_PATH=:/usr/local/lib
[11/17/21]seed@VM:~/.../Labsetup$ export TEST_VARIABLE='test'
[11/17/21]seed@VM:~/.../Labsetup$ env | grep TEST_VARIABLE
TEST_VARIABLE=test
[11/17/21]seed@VM:~/.../Labsetup$ nano foo.c
[11/17/21]seed@VM:~/.../Labsetup$ gcc foo.c
[11/17/21]seed@VM:~/.../Labsetup$ sudo chown root a.out
[11/17/21]seed@VM:~/.../Labsetup$ sudo chmod 4755 a.out
[11/17/21]seed@VM:~/.../Labsetup$ a.out > file6
[11/17/21]seed@VM:~/.../Labsetup$ env > file7
[11/17/21]seed@VM:~/.../Labsetup$ diff file6 file7
42a43
LD_LIBRARY_PATH=:/usr/local/lib
50c51
< =./a.out
---
 
=/usr/bin/env
```

## Task 6

We were able to run malicious code because the environment variable PATH was set to /home/seed.
We created a malicious script, named it 'ls' and placed it on the same directory as PATH.
The function would the call our script instead of the ls command.
Even though we set the owner of the file as root the malicious code doesn't run with root privileges because of a countermeasure that prevents a Set-UID program from receiving the owner's privileges.

```
[11/17/21]seed@VM:~$ nano ls
[11/17/21]seed@VM:~$ cat ls
#!/bin/bash

echo -e "Malicious code executed";
echo $(id);
exit 0;
[11/17/21]seed@VM:~$ ./ls
Malicious code executed
uid=1000(seed) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
[11/17/21]seed@VM:~$ chmod +x ls.sh
[11/17/21]seed@VM:~$ export PATH=/home/seed:$PATH
[11/17/21]seed@VM:~$ env | grep PATH
WINDOWPATH=2
LD_LIBRARY_PATH=:/usr/local/lib
PATH=/home/seed:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:.

[11/17/21]seed@VM:~/.../Labsetup$ cat foo.c
#include <stdlib.h>

int main()
{
   system("ls");
   return 0;
}
[11/17/21]seed@VM:~/.../Labsetup$ gcc foo.c
[11/17/21]seed@VM:~/.../Labsetup$ a.out > output
[11/17/21]seed@VM:~/.../Labsetup$ cat output
Malicious code executed
uid=1000(seed) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
```


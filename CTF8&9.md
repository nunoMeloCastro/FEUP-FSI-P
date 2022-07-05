# CTF realizado na Semana #8&9

## Desafio 1

The vulnerability exists in line 40 where we can manipulate de SQL query and bypass the website's authentication.

We know that if we manage to log as admin we will be presented with the flag.

We were having difficulties with concatenation characters so, in order to bypass this, we close the first condition and introduce a new OR condition with the desired username.

![image-48.png](./image-48.png)

![image-50.png](./image-50.png)

![image-49.png](./image-49.png)

## Desafio 2

We noticed that as an unauthenticated user we are able to perform a network speed test and ping a host.

![image-51.png](./image-51.png)

![image-52.png](./image-52.png)

What this functionality seems to do is run a ping command in the machine's terminal with our input.

With this knowledge we checked to see if our input was being sanitized and if not we could exploit this.

To test this we give it a website to the ping command followed by list of the root folder.

![image-53.png](./image-53.png)

![image-54.png](./image-54.png)

This worked as intended and we also found out that there was the file flag.txt at this location. The final step was to replace the ls command with a cat of that file.

![image-55.png](./image-55.png)

![image-56.png](./image-56.png)












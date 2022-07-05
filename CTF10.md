# CTF realizado na Semana #10

## Challenge 1

The first step to execute this attack was to investigate how the website worked. For that we inserted a random input on the field which led us to the following page.

![image-106.png](./image-106.png)

We are told that the admin needs to approve the request so the flag is shown and that means the "Give the flag" button needs to be pressed.
With that knowledge we inspected the source code of the page and found out that the id of that button is called "giveflag".

![image-107.png](./image-107.png)

The next step was to investigate out how to exploit this. We tried to input a script on the request field to see if there was a XSS vulnerability so that we could inject code which was proved to work.

![image-108.png](./image-108.png)

![image-109.png](./image-109.png)

The final was to build our attack script and retrieve the flag.

![image-110.png](./image-110.png)










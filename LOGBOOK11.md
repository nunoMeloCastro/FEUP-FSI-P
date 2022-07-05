# Trabalho realizado na Semana #10

## Task 1

We copied the openssl.cnf to our Labsetup directory and renamed it to myCA_openssl.cnf.
We the changed the default values to the ones below.

![image-74.png](./image-74.png)

We then ran the command provided in the guide in order to generate the self signed certificate for the certificate authority.

![image-75.png](./image-75.png)

From the output we identified the part that indicates that it is a CA's certificate.

![image-76.png](./image-76.png)

We also identified the part that indicates that it is a self signed certificate.

![image-77.png](./image-77.png)

Finally we located the modulus, both public and private exponent and both secret numbers.
We can see that all values, public and private, are shown in the key but only the public ones are shown in the csr.

![image-78.png](./image-78.png)

![image-79.png](./image-79.png)

![image-111.png](./image-111.png)

## Task 2

For this task we generated a CSR and key for our server, with the two alternative names added to the CSR.

![image-112.png](./image-112.png)

## Task 3

In this task we turned our CSR into a X509 certificate (crt) using our CA authorities key and crt.
We also uncommented the copy_extensions line in the config which will allow us to copy the extension fields to the final certificate.

![image-83.png](./image-83.png)

![image-82.png](./image-82.png)

We then confirmed that the alternative names are in fact in the crt.

![image-84.png](./image-84.png)

## Task 4

Based on the guide's example what we did first was to copy the server key and crt to apache2 docker container.

![image-85.png](./image-85.png)

We then made sure to rename these files and change their ownership to root. We also changed the apache server config in order to redirect to our website and to use our certificate and key.

![image-86.png](./image-86.png)

![image-87.png](./image-87.png)

We then enabled the ssl module and the sites described in the config file and started the apache server.

![image-88.png](./image-88.png)

First, we checked the HTTP site without ssl authentication which goes through port 80.

![image-89.png](./image-89.png)

And then checked the HTTPS site that goes through port 443 and does ssl authentication. This displayed us a warning that indicates that Firefox doesn't recognize our CA and after accepting and proceding with the warning we managed to go through.

![image-90.png](./image-90.png)

![image-91.png](./image-91.png)

We can bypass the warning by adding our CA to Firefox trusted CAs.

![image-92.png](./image-92.png)

![image-93.png](./image-93.png)

## Task 5

We simulated a DNS cache poisoning attack by changing /etc/hosts file on the victms machine however this only works over HTTP connection. Since firefox forces connection https on all URLs we have to manually type www.example.com in order to land on the compromised website

![image-111.png](./image-111.png)

![image-94.png](./image-94.png)

![image-95.png](./image-95.png)

![image-112.png](./image-112.png)

Firefox doesn't trust the CA but accepting the risk we are able to proceed.

![image-113.png](./image-113.png)

## Task 6

This experiment is simulated assuming the attacker managed to obtain facebook's certificate authority's private key. With this key we can generate the CA certificate and sign our own compromised web certificate.

![image-98.png](./image-98.png)

![image-99.png](./image-99.png)

The next step was to copy the compromised certificate and key to our apache web server where we create a new entry for a virtual host for facebook.com.

![image-100.png](./image-100.png)

![image-101.png](./image-101.png)

![image-102.png](./image-102.png)

The last step was to DNS cache poison the victim which was simulated by changing /etc/hosts file.

![image-103.png](./image-103.png)

Assuming that Firefox recognizes facebook's CA as secure we would have concluded our Man in the Middle attack successfully by HTTPS without any warnings.

![image-104.png](./image-104.png)




# Trabalho realizado na Semana #8&9

## Task 1
We ran the commands provided in the guide and with additional SQL ones we obtained the following.
![image-31.png](./image-31.png)
![image-32.png](./image-32.png)

## Task 2

### 2.1

To obtain the information of all the employees we had to bypass the authentication on the website. We were able to do that by inspecting the SQL query that is used to conduct user authentication.

![image-34.png](./image-34.png)

With this information we learned that if we logged as admin we would have access to all employees data.

![image-33.png](./image-33.png) 

We also found that we could manipulate the SQL query in the input and bypass the password field completely.

![image-35.png](./image-35.png)

![image-36.png](./image-36.png)

![image-37.png](./image-37.png)

### 2.2

The objective was the same as the previous one but now we had to achieve it through the command line.

Through the curl command and with some http URL encoding this is easily achieved. 

![image-38.png](./image-38.png)

### 2.3

We know that, in theory, through ';' we could run a second SQL command which is what we tried to do. However we got the same result every single time.

![image-39.png](./image-39.png)

After some investigation we discovered that there is a countermeasure. This countermeasure is the mysqli extension whose API does not allow multiple querys to run on the database server.

![image-40.png](./image-40.png)

## Task 3

### 3.1

The first part of this task is the same as in 2.1 task, which is to access an account. In this case Alice's.

![image-41.png](./image-41.png)

![image-42.png](./image-42.png)

Knowing that there is a column named salary, we can manipulate the SQL command through the edit fields.

![image-45.png](./image-45.png)

![image-46.png](./image-46.png)

![image-43.png](./image-43.png)

### 3.2

We can also manipulate Boby's salary the same way used to change Alice's.

![image-47.png](./image-47.png)

![image-44.png](./image-44.png)

We just need to add a WHERE clause to update only Boby's salary and comment the rest of the query with '#'.



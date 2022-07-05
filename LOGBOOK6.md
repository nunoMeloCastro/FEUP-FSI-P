# Trabalho realizado na Semana #5

## Task 1
We managed to get the format program crashing by inserting "%s" on the input, triggering invalid pointer access therefore crashing the program.

![image-11.png](./image-11.png)

## Task 2

### 2.A
Using a trial-error method we managed to find out the we needed 64 "%x" to print the first 4 bytes of our input.
In the beginning of the input we inserted "!!!!" which is equivalent to 0x21212121. With this we were able to easily locate the memory address on the stack the we could manipulate.

![image-12.png](./image-12.png)

![image-13.png](./image-13.png)

### 2.B
With the knowledge from the previous task we managed to print the secret message "A secret message" by inserting its address in the beginning of the input and changing the 64th output, which refers to the stack memory address of our myprintf() function, to "%s" therefore printing out the content of the target address.

![image-14.png](./image-14.png)

![image-15.png](./image-15.png)

## Task 3

### 3.A
Similarly to the previous task we managed to change the value of the target variable by inserting its address in the beginning of the input and changing the 64th output to "%n", which counts the number of characters printed till then (63 * 8 + 4 = 508 = 0x1cf), in order to change the value of the memory address location stored in the stack.

![image-17.png](./image-17.png)

![image-16.png](./image-16.png)

### 3.B
The procedure to this task is the same as the previous with a little difference. We have to make the program print 20480 (0x5000) characters before reaching "%n".
We do this by setting the last "%x" to "%.19980x" [20480 - (62 * 8 + 4) = 19980].

![image-18.png](./image-18.png)

![image-19.png](./image-19.png)

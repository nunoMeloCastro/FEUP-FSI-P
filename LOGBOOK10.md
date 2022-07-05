# Trabalho realizado na Semana #10

## Task 1

Using the information given in the instructions we logged into a account. We chose Alice's and then proceded to edit her profile.

![image-58.png](./image-58.png)

On the 'About me' field we wrote the given script but it wasn't working.
Soon we realised it was beacuse we were writing it in the visual editor instead of the HTML one.
After fixing this and saving the changes we got:

![image-59.png](./image-59.png)

This meant our script was probably working as intended.
To further prove this we logged onto another account to see if when we visited Alice´s profile it still worked. We chose Boby's.
 
 ![image-60.png](./image-60.png)

 ![image-61.png](./image-61.png)

 As expected the script still worked.

## Task 2

The process to executing this task was the same as the task before but now the goal was to display the user's cookies when viewing the compromised the account.
Again, in Alice's profile we modified the script to also include the given code to achieve the goal.

![image-62.png](./image-62.png)

![image-63.png](./image-63.png)

![image-64.png](./image-64.png)

## Task 3

In the previous task we were displaying the user's cookies but only he could see it, not the attacker so, using 'netcat' we opened a TCP server that would listen for a connection on a specified port.

![image-65.png](./image-65.png)

The next step was to alter our script so the attacker could retrieve that information.
Inserting an img tag, the browser tries to load the img from the specified URL resulting in sending a GET request to the attacker's machine.

![image-66.png](./image-66.png)

This script takes advantage of that and sends the cookies to the TCP server we set.
Right after saving the changes we got:

![image-67.png](./image-67.png)

## Task 4

The first step to executing this task was to understand how friend requests work.
With aid from the web developer tools we logged onto Boby's account and added Samy as a friend. 
Doing that revealed the following request:

![image-68.png](./image-68.png)

In this GET request we can see that parameters are sent on the URL.
We can see that the Id associated with Samy's account is 59.
We can also see that two tokens are also shown.

Using the sript template given in the instructions and completing it when a person visits Samy's account, an instant friend request should be made.

```
<script type="text/javascript">
window.onload = function () {
var Ajax=null;
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;
//Construct the HTTP request to add Samy as a friend.
var sendurl="http://www.seed-server.com/action/friends/add?friend=59"+ts+token;
//Create and send Ajax request to add friend
Ajax=new XMLHttpRequest();
Ajax.open("GET", sendurl, true);
Ajax.send();
}
</script>
```

![image-69.png](./image-69.png)

As soon we save the changes, the script runs and if we go to Samy's friends we see he is a friend of himself!

![image-70.png](./image-70.png)

We then logged onto another account to further prove the script was working properly.

![image-71.png](./image-71.png)

We then visited Samy's account and with the web developer tools found that the request to add him as a friend was being made.

![image-72.png](./image-72.png)

We finally went to see Alice's friends and she really was now friends with Samy!

![image-73.png](./image-73.png)

### Question 1

Those tokens are needed to verify if a HTTP request should be considered legitimate or not.

### Question 2

It wouldn't be possible because to run the script we need the script tags and in Editor mode special characters are encoded.









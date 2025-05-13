# nstuff
### CGI GET / POST data 

#### Replacement for the now defunct cgi MiniFieldStorage

## Parse GET and/or POST data into a dict

#### With a POST request you can parse POST data and the url query string. 
Example: Return POST and GET data from a request as JSON 
* nstuff.cgi
```py3
#!/usr/bin/env python3

"""
Example nstuff cgi script to show GET and POST data.

"""
import json
from nstuff import nstuff

if __name__ == '__main__':
    formstuff = nstuff()
    print("Content-type: text/Json\n")
    print(json.dumps(formstuff))


```
* GET
```js
a@fu:~$ curl  https://iodisco.com/cb/nstuff.cgi?you=me

{"you": "me"}

```
* POST
```js
a@fu:~$ curl -d "say"="Hey Koolaid" https://iodisco.com/cb/nstuff.cgi

{"say": "Hey Koolaid"}

```
* Both in a POST
```js
a@fu:~$ curl -d "say"="Hey Koolaid" https://iodisco.com/cb/nstuff.cgi?adrian=iscool

{"adrian": "iscool", "say": "Hey Koolaid"}

```

### The only method you need to call is nstuff() and it will return a dict of the request POST and GET vars . If you're just difficult, you can also call getstuff() or poststuff() directly and they will return the GET query string vars and POST data vars respectively.
![image](https://github.com/user-attachments/assets/227fb62c-d027-492b-a6b1-71c191bcb5b3)


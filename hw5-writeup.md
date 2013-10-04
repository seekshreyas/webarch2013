HW5 :: HTTP Data
==========================

_Author_ : Shreyas

_Email_ : shreyas@ischool.berkeley.edu


## Tasks with Telnet

- What HTTP command is used to make the /home resource respond with your full name (including spaces), the title of the page should be the full title of this class.
    - HTTP Command

```
    GET /home?name=Shreyas&title=Web%20Architecture HTTP/1.1
    Host: people.ischool.berkeley.edu
```

- Use a PUT request to set the redirect target of `http://people.ischool.berkeley.edu/~<USER>/server/wiki`
```
    PUT /wiki HTTP/1.1
    Host: localhost
    Content-Length:67 
    Content-Type: application/x-www-form-urlencoded

    url=http%3A%2F%2Fpeople.ischool.berkeley.edu%2F~shreyas%2Fserver%2Fwiki
```

- How do you verify this change?
    - Server responds with, which should be verified
        - `HTTP 200` making sure the request was `OK`
        - `Stored Wiki` in the response responds with the url supplied
```
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 66
    Server: Werkzeug/0.8.3 Python/2.7.3
    Date: Fri, 04 Oct 2013 03:43:17 GMT

    Stored wiki => http://people.ischool.berkeley.edu/~shreyas/server/Connection closed by foreign host.
```

- Use a POST to update the redirect target of http://people.ischool.berkeley.edu/~<USER>/server/wiki to a another new location


```
    POST /wiki HTTP/1.1
    Host:localhost
    Content-Length: 54
    Content-Type: application/x-www-form-urlencoded


    url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DBANUN31y2zY
```

-

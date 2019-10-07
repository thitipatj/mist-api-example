# mist-api-example
Example project for Mist API

Each python need configuration file to run. Please create "config.ini" with mandatory information. 
> Configuration file not included in this project.

Here's the component of the project:

## Configuration File Example:

```
[Global_Var]
ORG = 118cbf2b-xxxx-xxxx-xxxx-beee9a0220aa
SITE = 61982c4a-xxxx-xxxx-xxxx-bb281afa1620
TOKEN = biLXLTNTzG72G............TooxupUl4JkdnGVJ
MAP = b45a11b6-xxxx-xxxx-xxxx-df6dc5898906
```
## client.py
List a client stat on the screen, client by client, filter only focused key/value.

## ppsk.py
Example of the hospitality use case. Input full name of the guest, then the script will use his/her last name as a PPSK.

## ws-ex.py
Example of WebSocket connection to subscribe a stream of location of clients.

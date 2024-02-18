## AminoService
 A lib for creating amino bots and scripts ...

# How does this API work?

It works like the Amino.py's API but with added features 

# login SOURCE CODE

```python3
import AminoService

client = AminoService.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

print(client.profile.nickname)
```
# Discover userId , blogId and e.t.c from a link source code 

```python3
import AminoService

client = AminoService.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

# Url Example
# https://aminoapps.com/p/EXAMPLE

objectId = client.get_from_code("EXAMPLE").objectId
print(objectId)
```

# Send image and audio message source code

```python3
import AminoService

client = AminoService.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')
subclient = AminoService.SubClient(comId='COMMUNITY ID', profile=client.profile)

# Send Images
with open('file.png', 'rb') as file:
    subclient.send_message(message='MESSAGE', chatId='CHAT ID', file=file)

# Send Audios
with open('file.mp3', 'rb') as file:
    subclient.send_message(message='MESSAGE', chatId='CHAT ID', file=file, fileType="audio")

```
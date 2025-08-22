import base64

clientid = "xxx"
encoded = base64.b64encode(clientid.encode('utf-8'))
print(encoded.decode('utf-8'))

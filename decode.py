import base64

def decode(msg, key):
    print(base64.b64decode(msg))

msg =  '''DlcWEhYKBxwBTUFPUEIABwwDG1VGQVITCgsZDAMIBw9GVUpFQBAaFgoXBwQRV0lHUgwECR0YFQZX
RV1VTgsBERgEERkHCxBOTk9VCwIdGQAREAQHAQZNQU9QQhIbBQ0MGQ8FUlxFQAcIAA0bHhJSUF9H UhoDCRdNTVVXAwgaTkJVUk0WHB5EQAg='''
decode(msg, '')

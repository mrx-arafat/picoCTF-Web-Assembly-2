import requests

url = 'http://mercury.picoctf.net:7319/aD8SvhyVkb'
response = requests.get(url)
with open("webassembly_binary.wasm", "wb") as f:
    f.write(response.content)

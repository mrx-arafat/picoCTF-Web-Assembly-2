---
# Some Assembly Required 2

View Source Code carefully we get this [JS file](http://mercury.picoctf.net:7319/Y8splx37qY.js)

from there I got this..

`http://mercury.picoctf.net:7319/aD8SvhyVkb`

## Table of Contents

- [Requirements](#requirements)
- [Using Python](#using-python)
  - [Step 1: Fetch the WebAssembly Binary](#step-1-fetch-the-webassembly-binary)
  - [Step 2: Convert WebAssembly to Wat](#step-2-convert-webassembly-to-wat)
  - [Step 3: Interact with WebAssembly](#step-3-interact-with-webassembly)
  - [Step 4: Derive the Flag](#step-4-derive-the-flag)
- [Using CyberChef](#using-cyberchef)
  - [Step 1: Decode the Hexadecimal String](#step-1-decode-the-hexadecimal-string)
- [Conclusion](#conclusion)

## Requirements

- Basic understanding of Python programming.
- Access to the [CyberChef](https://gchq.github.io/CyberChef/) tool.
- Familiarity with WebAssembly concepts.

## Using Python

### Step 1: Fetch the WebAssembly Binary

To initiate the solution process, fetch the WebAssembly binary from the provided URL using the `requests` library:

```python
import requests

url = 'http://mercury.picoctf.net:7319/aD8SvhyVkb'
response = requests.get(url)
with open("webassembly_binary.wasm", "wb") as f:
    f.write(response.content)
```

### Step 2: Convert WebAssembly to Wat

Use the `wasm2wat` tool from the `wabt` toolset to convert the binary into a human-readable WebAssembly Text Format (Wat) file:

```
wasm2wat webassembly_binary.wasm -o readable.wat
```

### Step 3: Interact with WebAssembly

Interact with the WebAssembly binary using the `wasmer` library. This library enables you to call WebAssembly functions from Python. However, you need a solid understanding of the logic embedded in the WebAssembly module to utilize it effectively. (Inspect then Source Code View is the shortcut way to get `wasmer`)

### Step 4: Derive the Flag

Carefully analyze the `readable.wat` WebAssembly logic to decipher the flag. Understanding the operations and information used in the code will help you derive the correct flag. Here we get `xakgK\5cNs9=8:9l1?im8i<89?00>88k09=nj9kimnu\00\00`

## Using CyberChef

### Step 1: Decode the String

Utilize CyberChef >> `Magic` to decode the provided string.

1. Copy the srting: `xakgK\5cNs9=8:9l1?im8i<89?00>88k09=nj9kimnu\00\00`.
2. Open [CyberChef] (https://gchq.github.io/CyberChef/).
3. Magic in "Intensive Mode On" 
4. Crib (known plain text) set `pico`

`You will get the flag!!`
---

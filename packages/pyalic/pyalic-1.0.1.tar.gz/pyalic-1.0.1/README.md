# Pyalic: Advanced Licensing python module


Install package using `pip` from this GitHub repository

```shell
pip install pyalic
```



## Python example

```python
from pyalic import LicenseManager
import time

lm = LicenseManager("https://LICENSE_SERVER_URL.ORG", ssl_public_key='./trusted_cert.pem')


def my_program():
    print("Access granted!")
    time.sleep(30)


key = input("Enter your license key: ")
check_response = lm.check_key(key)
if check_response.success:
    my_program()
    lm.end_session()
else:
    print("Access denied:", check_response.error)
```

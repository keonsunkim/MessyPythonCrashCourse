"""
Python 3rd Party Package Library Imports
"""

import requests

"""
Sometimes you could create functionalities matching your own
needs. 
Or sometimes you could just use what others have made it 
availible to you.

Manytimes, reinventing the wheel can ba a very ineffecient choice.

The requests library consists of ways and already configured way to
communicate with the web. By utilizing this library we don't need to
write a code that communicate with the web from scratch. 

The above import will only run when we have the 3rd party package installed.

How to install the package for Windows:
Open CMD
Make sure you have python path option checked when installing python
Type "pip install requests" -> Enter
"""

s = requests.Session()
r = s.get('http://www.naver.com')

# by using two simple line of code, we can retrieve contents from
# websites thanks to the requests library!

print(r.status_code)
print(r.content)

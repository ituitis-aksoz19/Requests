###########################################################
#login assistant code, gathers values from a dic and tries#
###########################################################

import requests

url = "https://github.com/login"
user_name = ""
ids_passwords = {'exp_key': "exp_value"}
wadafak= 1   # i don't know the defaults

for i in ids_passwords.values():
    payload = {'username': user_name, 'pass': i}
    r = requests.get(url, data = payload, allow_redirects = True, timeout = wadafak)
    if r.status_code == requests.codes.ok:
        print("id =", user_name, "\npw =", i)
        break

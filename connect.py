import urllib.request
import urllib.parse
import re
import argparse
import getpass

parser = argparse.ArgumentParser(description="For login in type command: python connect.py --login --username=$usrname --password=$pass")

group = parser.add_mutually_exclusive_group()
group.add_argument("--login", action="store_true", help="login mode.")
group.add_argument("--logout", action="store_true", help="logout mode.")
args = parser.parse_args()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

if args.logout:
    request = urllib.request.Request("http://10.3.8.211/F.htm", headers=headers)
    response = urllib.request.urlopen(request)
elif args.login:
    username = input("Username: ")
    password = getpass.getpass("Password: ") 

    if username is None or password is None:
        print("Username or password not specified.")
        exit(1)
    data = urllib.parse.urlencode({
        "DDDDD": username,
        "upass": password,
        "0MKKey": "",
    }).encode("utf-8")
    request = urllib.request.Request("http://10.3.8.211", headers=headers)
    response = urllib.request.urlopen(request, data)

response_str = response.read().decode('gbk')
state = re.search("msga='(.*)'", response_str)
if state is None or state.group(1) == '':
    if args.logout:
        print("Successfully logged out.")
    elif args.login:
        print("Successfully logged in.")
else:
    print(state.group(1))
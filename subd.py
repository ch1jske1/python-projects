import requests
import sys

sub_list = open("subdomains-1000.txt").read()
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}"

    try:
        request.get{url_to_check}
    except requests.ConnectionError:
        pass
    else print("Valid domain",url_to_check)
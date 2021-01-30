import json
import re


def get_online_list(response):
    links = re.findall(r'<script>window.__INITIAL_STATE__=(.*?);\(function\(\)', response, re.S)[0]
    links = json.loads(links)
    return links
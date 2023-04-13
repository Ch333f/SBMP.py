#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Sofascore Basketball Match Prediction (SBMP) App


__author__ = "OTechCup"
__copyright__ = "Copyright 2022 - datetime.utcnow().year, OTechCup"
__credits__ = ["Mr. O."]
__license__ = "OTechCup"
__version__ = "os.environ.get('SBMPA_VERSION')"
__maintainer__ = "OTechCup"
__email__ = "help.otechcup@gmail.com"
__status__ = "os.environ.get('SBMPA_ENVIRONMENT_STATUS')"


# import modules
import requests

from itertools import cycle

from proxy_server import get_proxies


def initialize_proxy_sever() -> str:
    server = "https://free-proxy-list.net/"
    fetch_server = requests.get(server)
    
    return fetch_server.content

    
def initialize_sbmp_server() -> str:
    server = "https://www.sofascore.com/basketball"
    my_proxies = get_proxies()
    proxyPool = cycle(my_proxies) 
    
    #for i in range(1, 11):
    #    proxy = next(proxyPool)
    #    proxies = {'http': proxy, 'https': proxy}
    headers = {
        'User-Agent': (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/102.0.0.0 Safari/537.36"
        )
    }

    try:
        fetch_server = requests.get(server, headers=headers, timeout=10)
            
        return fetch_server.content
    except:
        return "Proxy Not Avaliable"

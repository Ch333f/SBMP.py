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
from scraper import parse_proxy_server


def get_proxies() -> set:
    server = parse_proxy_server()
    proxies = set()
    attrs = {'class': "table-striped"}
    
    for row in server.find("table", attrs=attrs).find_all("tr")[1:]:
        tds = row.find_all("td")  # table datas
        
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            
            proxies.add(str(ip) + ":" + str(port))
        except IndexError:
            continue
        
    return proxies

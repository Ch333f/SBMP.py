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
from bs4 import BeautifulSoup


def parse_proxy_server() -> str:
    server = initialize_proxy_sever()
    soup = BeautifulSoup(server, "lxml")
    
    return soup


def parse_sbmp_server() -> str:
    server = initialize_sbmp_server()
    soup = BeautifulSoup(server, "lxml")

    return str(soup)


# circular import modules
from crawler import initialize_proxy_sever, initialize_sbmp_server

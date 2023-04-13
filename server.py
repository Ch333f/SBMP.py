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
from flask import Flask
from dotenv import load_dotenv

import os

from scraper import parse_sbmp_server


load_dotenv()


sbmpa = Flask(__name__)
sbmpa.secret_key = os.environ.get("SBMPA_SECRET_KEY")


#print(parse_sbmp_server())


@sbmpa.route("/")
@sbmpa.route("/home", methods=['GET', 'POST'])
def index():
    return parse_sbmp_server()


if __name__ == '__main__':
    sbmpa.run(debug=True)

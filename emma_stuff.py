#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Accepts a comma separated string of fully qualified URLs and prints out a subset of those that are
incorrect along with the error code.
"""
from __future__ import unicode_literals

import argparse
import requests  # http://docs.python-requests.org/en/latest/api/
from requests.exceptions import ConnectionError


def check_urls(url_list):
    """Accepts a list of fully qualified URLs and returns a list of URLs that failed to return a
    successful status code.

    Args:
        url_list (list): A list of fully qualified URLs

    Returns:
        list: A list of bad URLs along with the status code if it's available.
    """
    bad_urls = []
    for url in url_list:
        try:
            response = requests.get(url)
        except requests.exceptions.HTTPError, exc:
            bad_urls.append("An error occurred trying to access the following URL: %s" % (url))
        if response.status_code >= 300:
            bad_urls.append("Unable to reach: %s an HTTP status code of %s was returned" %
                    (url, response.status_code))
    return bad_urls


def main():
    """Main"""
    parser = argparse.ArgumentParser(
        add_help=True, description="Parse a comma separated string of URLs and " \
            "return those that fail",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "--url-list", dest='urls', required=True,
        help='A comma separated list of URLs')
    args, _ = parser.parse_known_args()

    print("Validating URLs...")
    responses = check_urls(args.urls.split(','))
    for response in responses:
        print response

if __name__ == '__main__':
    main()


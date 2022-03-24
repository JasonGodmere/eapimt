# -*- coding: utf-8 -*-

import requests

AUTH = {}
BASE_URL = "https://api.enphaseenergy.com"


def format_uri(slug, **queries):
    # append queries to uri string, return result
    if not queries:
        return BASE_URL + slug

    query_str = ""
    for key, item in queries.items():
        # special case for first iteration
        if query_str == "":
            query_str = f"?{key}={item}"
        else:
            query_str += f"&{key}={item}"
    
    # create and return queried uri string
    return BASE_URL + slug + query_str


def get(slug, params={}, **queries):
    """
    Makes requests to enphase GET uri's

    Parameters
    ----------
    slug : str, required
        uri slug for enphase api request
    params : dict, required
        body params for requests
    """
    return requests.get(
        format_uri(slug, **queries),
        params=params,
        header=AUTH)


def post(slug, params={}, **queries):
    """
    Makes requests to enphase POST uri's

    Parameters
    ----------
    slug : str, required
        uri slug for enphase api request
    params : dict, required
        body params for requests
    """
    return requests.post(
        format_uri(slug, **queries),
        params=params,
        header=AUTH)


def put(slug, params={}, **queries):
    """
    Makes requests to enphase PUT uri's

    Parameters
    ----------
    slug : str, required
        uri slug for enphase api request
    params : dict, required
        body params for requests
    """
    return requests.put(
        format_uri(slug, **queries),
        params=params,
        header=AUTH)


def delete(slug, params={}, **queries):
    """
    Makes requests to enphase DELETE uri's

    Parameters
    ----------
    uri : str, required
        uri slug for enphase api request
    params : dict, required
        body params for requests
    """
    return requests.delete(
        format_uri(slug, **queries),
        params=params,
        header=AUTH)
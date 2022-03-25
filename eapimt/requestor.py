# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://api.enphaseenergy.com"
ACCESS = None
AUTH = None


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


def new_partner_token(email, password, client_id, client_secret):
    """
    Attempts authentication request with
    given credentails for new auth_token
    only for Enphase Partner Applications

    Parameters
    ----------
    email : str, required
        login email for account
    password : str, required
        login password for account
    client_id : str, required
        unique application client identifier
    client_secret : str, required
        unique application client secret key

    Returns
    -------
    success_indicator : bool
    """
    res = requests.post(format_uri("/oauth/token"),
            params={
                "grant_type": "password",
                "username": email,
                "password": password
            },
            auth=HTTPBasicAuth(client_id, client_secret))

    # filter for bad responses
    if res.status_code == 200:
        ACCESS = res.json()
        AUTH = {
            "Authorization": (
                ACCESS["token_type"] + " " + ACCESS["access_token"])
        }
        return True

    return False















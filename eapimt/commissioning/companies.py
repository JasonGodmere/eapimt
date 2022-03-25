# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def get_users(company_id):
    """
    makes request to -> 
        /api/v4/companies/{company_id}/users

    Get all users within a company

    Parameters
    ----------
    company_id : int, required
    	unique id of the company
    """
    res = requestor.get(
        f"/api/v4/companies/{company_id}/users")
    return res


def post_users(company_id, user):
    """
    makes request to -> 
        /api/v4/companies/{company_id}/users

    Create company user

    Parameters
    ----------
    company_id : int, required
    	unique id of the company
    user : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.post(
        f"/api/v4/companies/{company_id}/users",
        data=user)
    return res


def get_user_id(company_id, user_id, **kwargs):
    """
    makes request to -> 
        /api/v4/companies/{company_id}/
        users/{user_id}

    Returns the requested user

    Parameters
    ----------
    company_id : int, required
    	unique id of the company
    user_id : int, required
        unique id of the user
    expand : str, optional
        expand return params.
        available values: company
    """
    res = requestor.get(
        f"/api/v4/companies/{company_id}/users/{user_id}",
        **kwargs)
    return res


def put_user_id(company_id, user_id, user):
    """
    makes request to -> 
        /api/v4/companies/{company_id}/users/{user_id}

    Update company user

    Parameters
    ----------
    company_id : int, required
    	unique id of the company
    user_id : int, required
        unique id of the user
    user : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.put(
        f"/api/v4/companies/{company_id}/users/{user_id}",
        data=user)
    return res


def get_branches():
    """
    makes request to -> 
        /api/v4/companies/self/branches

    API user's company and its branches

    Parameters
    ----------
    None
    """
    res = requestor.get(
        "/api/v4/companies/self/branches")
    return res
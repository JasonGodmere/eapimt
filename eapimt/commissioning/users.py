# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def get_activations_user_id(activation_id, user_id, **kwargs):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/users/
        {user_id}

    You must have access to the requested activation 
    and user; otherwise a 401 is returned. The user 
    is requested in the scope of an activation, then 
    it must be the owner or the host of an activation 
    the API user can manage (or) Users created by API 
    user (or) Users who belong to your company or its 
    branches.

    Parameters
    ----------
    activation_id : int, required
        unique id of an enphase system (system_id)
    user_id : int, required
    	unique id of an enphase user
    expand : int, optional
    	Passing expand params in the url with valid 
    	option, then the response will contain company 
    	object fields. values: company
    """
    res = requestor.get(
        f"/api/v4/activations/{activation_id}/users/{user_id}",
        **kwargs)
    return res


def put_activations_user_id(activation_id, user_id, user):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/users/
        {user_id}

    Update user

    Parameters
    ----------
    activation_id : int, required
        unique id of an enphase system (system_id)
    user_id : int, required
    	unique id of an enphase user
    user : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.put(
        f"/api/v4/activations/{activation_id}/users/{user_id}",
        data=user)
    return res


def get_search(**kwargs):
    """
    makes request to -> 
        /api/v4/users/search

    Search User

    Parameters
    ----------
    email : str, optional
    	Email of user
    """
    res = requestor.get(
        "/api/v4/users/search",
        **kwargs)
    return res


def get_user_id(user_id, **kwargs):
    """
    makes request to -> 
        /api/v4/users/{user_id}

    Returns the requested user

    Parameters
    ----------
    user_id : int, required
    	unique id of an enphase user
    expand : int, optional
    	Passing expand params in the url with valid 
    	option, then the response will contain company 
    	object fields. values: company
    """
    res = requestor.get(
        f"/api/v4/users/{user_id}",
        **kwargs)
    return res


def put_user_id(user_id, user):
    """
    makes request to -> 
        /api/v4/users/{user_id}

    Update user

    Parameters
    ----------
    user_id : int, required
    	unique id of an enphase user
    user : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.put(
        f"/api/v4/users/{user_id}",
        data=user)
    return res


def get_self(**kwargs):
    """
    makes request to -> 
        /api/v4/users/self

    Return the current logged in
    user details

    Parameters
    ----------
    expand : int, optional
    	Passing expand params in the url with valid 
    	option, then the response will contain company 
    	object fields. values: company
    """
    res = requestor.get(
        f"/api/v4/users/self",
        **kwargs)
    return res
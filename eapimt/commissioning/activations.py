# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def get(**kwargs):
    """
    makes request to -> 
        /api/v4/partner/activations

    Returns a list of activations for which the 
    user can make API requests.

    Parameters
    ----------
    next : str, optional
    	If the first request does not return a 
    	full list, use the 'next' attribute in 
    	the response body to request the next page.
    limit : int, optional
    	There is a limit to the number of activations 
    	which can be returned at one time
    stage : str, optional
    	Filter activations by stage. available
    	values: 1,2,3,4
    reference : str, optional
    	Filter activations by company reference
    installer_id : int, optional
    	filter activations by installer id
    system_name : str, optional
    	filter activations by system name
    address : str, optional
    	filter activations by address. Will perform
    	partial search on street1, street2, country,
    	state and zipcode
    region : str, optional
    	filter activations by region. see docs for 
    	details
    search : str, optional
    	filter activations by search. Will perform 
    	partial search with system_name, reference,
    	system_id, street1, street2, country, state,
    	zipcode
    """
    res = requestor.get(
        "/api/v4/partner/activations",
        **kwargs)
    return res


def post(system):
    """
    makes request to -> 
        /api/v4/partner/activations

    Create new activation

    Parameters
    ----------
    system : object, required
    	see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.post(
        "/api/v4/partner/activations",
        data=system)
    return res


def get_id(id, **kwargs):
    """
    makes request to -> 
        /api/v4/partner/activations/{id}

    Retrieves an activation by id

    Parameters
    ----------
    id : int, required
    	The Enlighten ID of the system
    expand : str, optional
        add values to response. values:
        owner, owner.company, host,
        host.company
    """
    res = requestor.get(
        f"/api/v4/partner/activations/{id}",
        **kwargs)
    return res


def put_id(id, system, **kwargs):
    """
    makes request to -> 
        /api/v4/partner/activations/{id}

    Update an activation

    Parameters
    ----------
    id : int, required
    	The Enlighten ID of the system
    system : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.put(
        f"/api/v4/partner/activations/{id}",
        data=system,
        **kwargs)
    return res


def delete_id(id):
    """
    makes request to -> 
        /api/v4/activations/{id}

    Delete an activation by id

    Parameters
    ----------
    id : int, required
    	unique id of activation/system
    """
    res = requestor.delete(
        f"/api/v4/activations/{id}")
    return res


def post_user_id(activation_id, user_id):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/
        users/{user_id}

    Grant access a user access to activation
    by user_id

    Parameters
    ----------
    activation_id : int, required
    	unique id of activation/system
    user_id : int, required
        unique id of the user
    """
    res = requestor.post(
        f"/api/v4/activations/{activation_id}/users/{user_id}")
    return res


def delete_user_id(activation_id, user_id):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/
        users/{user_id}

    Revoke access of a user from activation

    Parameters
    ----------
    activation_id : int, required
    	unique id of activation/system
    user_id : int, required
        unique id of the user
    """
    res = requestor.delete(
        f"/api/v4/activations/{activation_id}/users/{user_id}")
    return res


def post_production_mode(activation_id, production_mode):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/
        ops/production_mode

    Set production mode

    Parameters
    ----------
    activation_id : int, required
    	unique id of activation/system
    production_mode : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.post(
        f"/api/v4/activations/{activation_id}/ops/production_mode",
        data=production_mode)
    return res


def get_production_mode(activation_id):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/
        ops/production_mode

    Get production mode

    Parameters
    ----------
    activation_id : int, required
    	unique id of activation/system
    """
    res = requestor.get(
        f"/api/v4/activations/{activation_id}/ops/production_mode")
    return res
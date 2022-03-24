# -*- coding: utf-8 -*-

import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def activations(**kwargs):
    """
    makes request to -> 
        /api/v4/partner/activations

    Returns a list of activations for which the 
    user can make API requests.

    By default, activations are returned in batches 
    of 100. The maximum page size is 1000.

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


def activations_user(activation_id, user_id, **kwargs):
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



















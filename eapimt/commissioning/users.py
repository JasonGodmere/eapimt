# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def get_user(activation_id, user_id, **kwargs):
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

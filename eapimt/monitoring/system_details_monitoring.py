# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def get_systems(**kwargs):
    """
    makes request to -> 
        /api/v4/systems

    Returns a list of systems for which the user 
    can make API requests. By default, systems 
    are returned in batches of 10. The maximum 
    size is 100.

    Parameters
    ----------
    page (query) : int, optional
        The page to be returned (default=1, min=1)
    size (query) : int, optional
        Maximum number of records shown per page 
        (default=10, min=1, max=100)
    sort_by (query) : str, optional
        Returns list of systems sorted by <sort_by> 
        field. To get ASC order sorted list, user 
        sort_by = . To get DESC order sorted list, 
        use sort_by = (-). Current sort keys 
        supported are id, name, and last_report_date. 
        By default the list is sorted by decreasing 
        system ID.

        Available values : 
            id, name, last_report_date, -id, -name, 
            -last_report_date
    """
    res = requestor.get(
        "/api/v4/systems",
        **kwargs)
    return res


def search(params={}, **kwargs):
    """
    makes request to ->
        /api/v4/systems/search

    Search and filter systems. Provide only valid 
    values in request parameters. Empty and invalid 
    values will be ignored. Invalid keys will be 
    rejected.

    Parameters
    ----------
    page : int, optional
        The page to be returned (default=1, min=1)
    size : int, optional
        Maximum number of records shown per page 
        (default=10, min=1, max=100)
    params : dict, optional
        See developer-v4.enphase.com/docs under
        systems/search for details on usage
    """
    res = requestor.get(
        "/api/v4/systems/search",
        data=params,
        **kwargs)
    return res


def system_id(system_id):
    """
    makes request to -> 
        /api/v4/systems/{system_id}

    Retrieves a system by system_id

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}")
    return res


def summary(system_id):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/summary

    Returns system summary based on the specified 
    system_id.

    Parameters
    ----------
    system_id (path) : int, required
        unique id of an enphase system
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/summary")
    return res


def devices(system_id):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/devices

    Retrieves devices for a given system. Only 
    devices that are active will be returned in 
    the response.

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/devices")
    return res


def retrieve_system_id(serial_num):
    """
    makes request to -> 
        /api/v4/systems/retrieve_system_id

    Get system ID by passing gateway serial number. 
    If the serial number of a retired envoy is 
    passed in the request param, a 404 Not Found 
    response will be returned.

    Parameters
    ----------
    serial_num : int, required
        unique id of gateway monitor
    """
    res = requestor.get(
        f"/api/v4/systems/retrieve_system_id",
        serial_num=serial_num)
    return res


def inverters_summary(**kwargs):
    """
    makes request to -> 
        /api/v4/systems/inverters_summary
        _by_envoy_or_site

    Returns the microinverters summary based on 
    the specified active gateway serial number or 
    system ID.

    Parameters
    ----------
    NOTE: Only one of the two params are necessary
    site_id : int, required
        unique id of an enphase system
    envoy_serial_number : int, required
        serial number of system gateway
    """
    res = requestor.get(
        f"/api/v4/systems/inverters_summary_by_envoy_or_site",
        **kwargs)
    return res













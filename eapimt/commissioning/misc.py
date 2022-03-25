# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


### Home Owner ###

def post_home_owner(user):
    """
    makes request to -> 
        /api/v4/users

    Create home owner

    Parameters
    ----------
    user : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.post(
        "/api/v4/users",
        data=user)
    return res


### Estimate ###

def get_estimate(activation_id):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/estimate

    Returns the estimate for this
    system (production)

    Parameters
    ----------
    activation_id : int, required
        unique id of system
    """
    res = requestor.get(
        f"/api/v4/activations/{activation_id}/estimate")
    return res


def put_estimate(activation_id, estimate):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/estimate

    Update the estimate for this
    system (production)

    Parameters
    ----------
    activation_id : int, required
        unique id of system
    estimate : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.get(
        f"/api/v4/activations/{activation_id}/estimate",
        data=estimate)
    return res


### Grid Profiles ###

def get_grid_profiles():
    """
    makes request to -> 
        /api/v4/grid_profiles

    Lists the available profiles

    Parameters
    ----------
    None
    """
    res = requestor.get(
        "/api/v4/grid_profiles")
    return res


### Meters ###

def get_meters(system_id, serial_number):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/meters/
        {serial_number}

    Returns the requested meter
    details

    Parameters
    ----------
    system_id : int, required
        unique id of the system
    serial_number : str, required
        serial number of meter
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/meters/{serial_number}")
    return res


def put_meters(system_id, serial_number, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/meters/
        {serial_number}

    Update the operational date of a 
    meter by serial number

    Parameters
    ----------
    system_id : int, required
        unique id of the system
    serial_number : str, required
        serial number of meter
    """
    res = requestor.put(
        f"/api/v4/systems/{system_id}/meters/{serial_number}",
        **kwargs)
    return res


def post_meter_control(activation_id, serial_number, params):
    """
    makes request to -> 
        /api/v4/activations/{activation_id}/
        meters/{serial_number}/meter_control

    Enable or disable a meter

    Parameters
    ----------
    activation_id : int, required
        unique id of the system
    serial_number : str, required
        serial number of meter
    params : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.post(
        f"/api/v4/activations/{activation_id}/meters/{serial_number}/meter_control",
        data=params)
    return res


### PvManufacturers ###

def get_pv_manufacturers():
    """
    makes request to -> 
        /api/v4/pv_manufacturers

    Returns PV module manufacturers

    Parameters
    ----------
    None
    """
    res = requestor.get(
        "/api/v4/pv_manufacturers")
    return res


### PvModels ###

def get_pv_models(pv_manufacturer_id):
    """
    makes request to -> 
        /api/v4/pv_manufacturers/{pv_manufacturer_id}
        /pv_models

    Returns PV module manufacturers

    Parameters
    ----------
    pv_manufacturer_id : int, required
        unique id of pv manufacturer
    """
    res = requestor.get(
        f"/api/v4/pv_manufacturers/{pv_manufacturer_id}/pv_models")
    return res


### Tariff ###

def get_tariff(system_id):
    """
    makes request to -> 
        /api/v4/systems/config/{system_id}
        /tariff

    Get tariff for a system

    Parameters
    ----------
    system_id : int, required
        unique id of system
    """
    res = requestor.get(
        f"/api/v4/systems/config/{system_id}/tariff")
    return res


def put_tariff(system_id, params):
    """
    makes request to -> 
        /api/v4/systems/config/{system_id}
        /tariff

    Get tariff for a system

    Parameters
    ----------
    system_id : int, required
        unique id of system
    params : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.put(
        f"/api/v4/systems/config/{system_id}/tariff",
        data=params)
    return res


### Arrays ###

def get_arrays(system_id):
    """
    makes request to -> 
        /api/v4/systems/{system_id}
        /arrays

    Fetch particular system array
    details

    Parameters
    ----------
    system_id : int, required
        unique id of system
    """
    res = requestor.get(
        "/api/v4/systems/{system_id}/arrays")
    return res


def put_arrays(system_id, params):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/
        arrays

    Update all arrays for system

    Parameters
    ----------
    system_id : int, required
        unique id of system
    params : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.put(
        f"/api/v4/systems/{system_id}/arrays",
        data=params)
    return res


def get_arrays_id(system_id, id):
    """
    makes request to -> 
        /api/v4/systems/{system_id}
        /arrays/{id}

    Fetch array details by id

    Parameters
    ----------
    system_id : int, required
        unique id of system
    id : int, required
        unique id of array
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/arrays/{id}",
        **kwargs)
    return res


def put_arrays_id(system_id, id, params):
    """
    makes request to -> 
        /api/v4/systems/{system_id}
        /arrays/{id}

    Update particular system array
    details

    Parameters
    ----------
    system_id : int, required
        unique id of system
    id : int, required
        unique id of array
    params : object, required
        see https://developer-v4.enphase.com/docs
        for details
    """
    res = requestor.put(
        f"/api/v4/systems/{system_id}/arrays/{id}",
        data=params)
    return res
    

def delete(system_id, id):
    """
    makes request to -> 
        /api/v4/systems/{system_id}
        /arrays/{id}

    Delete an array by id

    Parameters
    ----------
    system_id : int, required
        unique id of system
    id : int, required
        unique id of array
    """
    res = requestor.delete(
        f"/api/v4/systems/{system_id}/arrays/{id}")
    return res
# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def consumption_lifetime(system_id, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/
        consumption_lifetime

    Returns a daily time series of energy 
    consumption as measured by the consumption 
    meter installed on the specified system. 
    All measurements are in Watt hours.

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    start_date : str, optional (default=operational
                                            _date)
        start date of reporting period with 
        YYY-MM-DD format
    end_date : str, optional (default=operational
                                            _date)
        end date of reporting period with YYYY-MM-DD
        format
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/consumption_lifetime",
        **kwargs)
    return res


def consumption_meter(system_id, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/telemetry/
        consumption_meter

    Retrieves telemetry for all the consumption 
    meters of a system. If the start_at specified 
    is earlier than the system's first reported 
    date, then midnight of the system's first 
    reported date is considered as start_at. 
    The end_at is calculated as the minimum of the 
    time of the request and (start time + 
    granularity).

    The requested start date must be within 2 years 
    from current date.

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    start_at : int, optional (default=midnight)
        Start time for fetching the telemetry data 
        in Epoch time format.
    granularity : str, optional (default=day)
        The granularity of the telemetry data. 
        Possible values are 'week', 'day', '
        15mins'. Default is 'day'
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/telemetry/consumption_meter",
        **kwargs)
    return res




















    
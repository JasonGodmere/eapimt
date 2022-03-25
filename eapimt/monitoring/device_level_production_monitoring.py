# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def micro_telemetry(system_id, serial_no, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/devices/
        micros/{serial_no}/telemetry

    Retrieves telemetry for single micro/pcu.

    If granularity is 15mins, maximum 3 intervals 
    will appear in response. If granularity is day, 
    maximum 288 intervals will appear in response 
    where each interval is of 5 mins duration.

    The requested start date must be within 2 years 
    from current date

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    serial_no : str, required
        Serial number of the individual solar
        microinverter
    start_at : int, optional (default=midnight)
        Start time for fetching the telemetry data 
        in Epoch time format.
    granularity : str, optional (default=day)
        The granularity of the telemetry data. 
        Possible values are 'week', 'day', '
        15mins'. Default is 'day'
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/devices/micros/{serial_no}/telemetry",
        **kwargs)
    return res


def acb_telemetry(system_id, serial_no, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/devices/
        acbs/{serial_no}/telemetry

    Retrieves telemetry for single ACB.

    If granularity is 15mins, maximum 3 intervals 
    will appear in response. If granularity is day, 
    maximum 288 intervals will appear in response 
    where each interval is of 5 mins duration.

    The requested start date must be within 2 years 
    from current date

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    serial_no : str, required
        Serial number of the acb
    start_at : int, optional (default=midnight)
        Start time for fetching the telemetry data 
        in Epoch time format.
    granularity : str, optional (default=day)
        The granularity of the telemetry data. 
        Possible values are 'week', 'day', '
        15mins'. Default is 'day'
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/devices/acbs/{serial_no}/telemetry",
        **kwargs)
    return res


def encharge_telemetry(system_id, serial_no, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/devices/
        encharges/{serial_no}/telemetry

    Retrieves telemetry for single Encharge.

    If granularity is 15mins, maximum 3 intervals 
    will appear in response. If granularity is day, 
    maximum 288 intervals will appear in response 
    where each interval is of 5 mins duration.

    The requested start date must be within 2 years 
    from current date

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    serial_no : str, required
        Serial number of the acb
    start_at : int, optional (default=midnight)
        Start time for fetching the telemetry data 
        in Epoch time format.
    granularity : str, optional (default=day)
        The granularity of the telemetry data. 
        Possible values are 'week', 'day', '
        15mins'. Default is 'day'
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/devices/encharges/{serial_no}/telemetry",
        **kwargs)
    return res













    
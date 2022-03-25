# -*- coding: utf-8 -*-

from .. import requestor

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


### Site Level Production Monitoring ###

def production_meter_readings(system_id):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/
        production_meter_readings

    Returns the last known reading of each 
    production meter on the system as of the 
    requested time, regardless of whether the 
    meter is currently in service or retired.

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/production_meter_readings")
    return res


def rgm_stats(system_id, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/rgm_stats

    Returns performance statistics as measured 
    by the revenue-grade meters installed on 
    the specified system.

    Parameters
    ----------
    system_id : int, required
        unique id of an enphase system
    start_at : int, optional (default=midnight)
        start of reporting period in unix epoch
        time.
    end_at : int, optional (default=start_at+1week)
        end of reporting period in unix epoch time.
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/rgm_stats",
        **kwargs)
    return res


def energy_lifetime(system_id, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/energy_lifetime

    Returns a daily time series of energy produced 
    by the system over its lifetime. All 
    measurements are in Watt hours.

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
    production : str (default=ignored)
        When “all”, returns the merged time series 
        plus the time series as reported by the 
        microinverters and the meter on the system. 
        Other values are ignored.
    """
    res = requestor.get(
        f"/api/v4/systems/{system_id}/energy_lifetime",
        **kwargs)
    return res


def production_micro(system_id, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/telemetry/
        production_micro

    Retrieves telemetry for all the production 
    micros of a system. If no start_at is specified, 
    defaults to midnight today, in the timezone of 
    the system.

    The requested start date must be within 2 years 
    from current date.

    The end_at is calculated as the minimum 
    of the time of the request and 
    (start time + granularity).

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
        f"/api/v4/systems/{system_id}/telemetry/production_micro",
        **kwargs)
    return res


def production_meter(system_id, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/telemetry/
        production_meter

    Retrieves telemetry for all the production 
    meters of a system.

    The end_at is calculated as the minimum 
    of the time of the request and 
    (start time + granularity).

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
        f"/api/v4/systems/{system_id}/telemetry/production_meter",
        **kwargs)
    return res


def battery(system_id, **kwargs):
    """
    makes request to -> 
        /api/v4/systems/{system_id}/telemetry/
        battery

    Retrieves telemetry for all the batteries 
    of a system.

    The end_at is calculated as the minimum 
    of the time of the request and 
    (start time + granularity).

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
        f"/api/v4/systems/{system_id}/telemetry/battery",
        **kwargs)
    return res















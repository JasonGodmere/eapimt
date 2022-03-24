# -*- coding: utf-8 -*-

import requestor

## DOCSTRINGS

### System Details - Requests ###
# Refer to https://developer-v4.enphase.com/docs 
# for details


def systems(**kwargs):
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


def search(**kwargs):
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
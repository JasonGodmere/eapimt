# -*- coding: utf-8 -*-
from . import helpers


## USE DOCSTRINGS

def fetch_systems(page, size, sort_by):
    """
    makes request to -> /api/v4/systems

    Parameters
    ----------
    page : int, optional
        The page to be returned (default=1, min=1)
    size : int, optional
        Maximum number of records shown per page 
        (default=10, min=1, max=100)
    sort_by : str, optional
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

    Returns
    -------
    response
    """
    pass
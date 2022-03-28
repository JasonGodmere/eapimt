# EAPIMT

This tool is in no way affiliated with Enphase, it is intended for use in the open source community as a simplified way of interfacing and using their api service.

In hindsight the only real useful code comes from requestor.py.
With more intuitive path structure on the Enphase API it may have made sense to have explicit functions for each path, but the complexity of categorization and quantity of calls turned out to be more work than it's worth.

## Installation

Clone the repository

```bash
git@github.com:JasonGodmere/eapimt.git
```
or
```bash
https://github.com/JasonGodmere/eapimt.git
```

Then setup and install the package into the current 
python environment.

```bash
python setup.py install
```

## Basic Usage

```bash
import eapimt.requestor as req

# setup enphase connection parameters
req.Access.init(api_key, client_id, client_secret)

# make request for new OAuth2.0 access token
# requires the email and password of API account
req.Access.new_partner_token(email, password)

# now you are ready to make requests
res = req.get("/api/v4/partner/activations")
```

## Advanced Usage

See docs for full information on available
request functions

```bash
import eapimt.monitoring as mon
from eapimt.commissioning import (
    activations,
    companies,
    users,
    misc
)
import eapimt.requestor as req

# setup enphase connection parameters
req.Access.init(api_key, client_id, client_secret)

# make request for new OAuth2.0 access token
# requires the email and password of API account
req.Access.new_partner_token(email, password)

# make a request
## Retrieve an activation by id
res = activations.get_id(activation_id)

```
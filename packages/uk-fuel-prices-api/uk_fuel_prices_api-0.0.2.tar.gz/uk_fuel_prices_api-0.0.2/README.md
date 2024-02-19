# UK Fuel Prices

Pull UK Fuel Price data from sources listed [here](https://www.gov.uk/guidance/access-fuel-price-data). Please note the data is not complete, and does not include pricing for every fuel station in the UK. More information is available at the link.

## Installation
The package is available to install with `pip`

```python
pip install uk-fuel-prices-api
```

## Example

### Initialise
Import the package, and retrieve price information. `get_prices()` should be called whenever you want to update the pricing data. Please bear in mind that at this time, most companies are only updating their data feeds every 24 hours.
```python
from uk_fuel_prices_api import UKFuelPricesApi
api = UKFuelPricesApi();

await api.get_prices()
```

### Search
Search for all stations matching value
```python
await api.search("searchstring")

# Only return first 5 results
await api.search("searchstring", 5)
```

### Site ID
Get single Station by known site_id
```python
await api.get_site_id("siteid")
```

# UK Fuel Prices

Pull UK Fuel Price data from sources listed [here](https://www.gov.uk/guidance/access-fuel-price-data).

## Example

### Initialise

```python
from uk_fuel_prices_api import UKFuelPricesApi
api = UKFuelPricesApi();

await api.get_all_endpoints_dataframe()
```

### Search
```python
# Search for all stations matching value
await api.search("searchstring")

# Only return first 5 results
await api.search("searchstring", 5)
```

### Site ID
```python
# Get single Station by known site_id
await api.get_site_id("siteid")
```

### Nearest
```python
# Find the nearest fuel stations to a lat,lng location
my_lat = 53.483959
my_lng = -2.244644
number_of_stations_to_return = 10

stations = api.nearest(my_lat, my_lng, number_of_stations_to_return)

display (stations)
```
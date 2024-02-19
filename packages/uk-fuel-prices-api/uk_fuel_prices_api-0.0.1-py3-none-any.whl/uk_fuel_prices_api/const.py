"""Constants"""

# Endpoints
# @see https://www.gov.uk/guidance/access-fuel-price-data
APPLEGREEN = "https://applegreenstores.com/fuel-prices/data.json"
ASCONA_GROUP = "https://fuelprices.asconagroup.co.uk/newfuel.json"
ASDA = "https://storelocator.asda.com/fuel_prices_data.json"
BP = "https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json"
ESSO_TESCO_ALLIANCE = "https://fuelprices.esso.co.uk/latestdata.json"
MORRISONS = "https://www.morrisons.com/fuel-prices/fuel.json"
MOTO = "https://moto-way.com/fuel-price/fuel_prices.json"
MOTOR_FUEL_GROUP = "https://fuel.motorfuelgroup.com/fuel_prices_data.json"
RONTEC = (
    "https://www.rontec-servicestations.co.uk/fuel-prices/data/fuel_prices_data.json"
)
SAINSBURYS = "https://api.sainsburys.co.uk/v1/exports/latest/fuel_prices_data.json"
SGN = "https://www.sgnretail.uk/files/data/SGN_daily_fuel_prices.json"
SHELL = "https://www.shell.co.uk/fuel-prices-data.html"
TESCO = "https://www.tesco.com/fuel_prices/fuel_prices_data.json"

ALL_ENDPOINTS = [
    APPLEGREEN,
    ASCONA_GROUP,
    ASDA,
    BP,
    ESSO_TESCO_ALLIANCE,
    MORRISONS,
    MOTO,
    MOTOR_FUEL_GROUP,
    RONTEC,
    SAINSBURYS,
    SGN,
    SHELL,
    TESCO,
]

FUEL_TYPES = {"B7": "Diesel", "E5": "E5 Petrol", "E10": "E10 Petrol", "SDV": "SDV"}

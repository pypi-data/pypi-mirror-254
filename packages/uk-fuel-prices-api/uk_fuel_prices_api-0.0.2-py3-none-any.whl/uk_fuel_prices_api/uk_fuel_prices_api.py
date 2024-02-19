"""UK Fuel Price API."""

import asyncio
import aiohttp
import logging

import pandas as pd

from .const import ALL_ENDPOINTS

_LOGGER = logging.getLogger(__name__)


class UKFuelPricesApi:
    """UK Fuel Prices API."""

    def __init__(self) -> None:
        """Initialise UK Fuel Price API."""
        self.stations = pd.DataFrame
        self.session: aiohttp.ClientSession

    async def __get_endpoint_dataframe(self, endpoint: str) -> pd.DataFrame:
        """Fetch data from a single endpoint."""
        try:
            response = await self.session.get(endpoint)
            json = await response.json(content_type=None)
        except asyncio.TimeoutError:
            _LOGGER.error("Timeout fetching %s", endpoint)
            return None

        stations = pd.DataFrame.from_dict(json["stations"])
        stations["last_updated"] = json["last_updated"]

        stations = stations.join(pd.json_normalize(stations["location"])).drop(
            "location", axis="columns"
        )
        stations = stations.join(pd.json_normalize(stations["prices"])).drop(
            "prices", axis="columns"
        )

        return stations

    async def get_prices(self) -> bool:
        """Query all endpoints for fuel station prices."""
        # _LOGGER.debug("get_all_endpoints_dataframe")

        station_dfs = []
        self.stations = pd.DataFrame

        await self.__open_session()

        for endpoint in ALL_ENDPOINTS:
            df = await self.__get_endpoint_dataframe(endpoint)
            station_dfs.append(df)

        await self.__close_session()

        self.stations = pd.concat(station_dfs, ignore_index=True)

        self.stations["latitude"] = pd.to_numeric(self.stations["latitude"])
        self.stations["longitude"] = pd.to_numeric(self.stations["longitude"])

        self.__correct_pence_to_pounds()

        return self.stations.size > 0

    def __correct_pence_to_pounds(self):
        """Correct any values returned in pence to pounds."""
        ASSUME_POUNDS_IF_OVER = 10

        self.stations.loc[self.stations.B7 > ASSUME_POUNDS_IF_OVER, "B7"] = (
            self.stations["B7"] / 100
        )

        self.stations.loc[self.stations.E10 > ASSUME_POUNDS_IF_OVER, "E10"] = (
            self.stations["E10"] / 100
        )

        self.stations.loc[self.stations.E5 > ASSUME_POUNDS_IF_OVER, "E5"] = (
            self.stations["E5"] / 100
        )

        self.stations.loc[self.stations.SDV > ASSUME_POUNDS_IF_OVER, "SDV"] = (
            self.stations["SDV"] / 100
        )

    def search(self, value: str, n: int = 10) -> pd.DataFrame:
        """Search stations for a given value string."""

        mask = (
            self.stations[["brand", "address", "postcode"]]
            .apply(lambda x: x.str.contains(value, case=False))
            .any(axis=1)
        )

        return self.stations[mask].head(n)

    def nearest(self, my_lat: float, my_lng: float, n: int = 5) -> dict:
        """Find n Nearest Fuel Stations to Given Location."""
        stations = self.stations.copy()

        # quick pythagoras hack, won't work for stations a long way away
        #  as no allowance for curvature of earth
        stations["dist"] = pow(my_lat - stations["latitude"], 2) + pow(
            my_lng - stations["longitude"], 2
        )

        stations = stations.sort_values(by="dist")

        return stations.head(n).to_dict("records")

    def get_site_id(self, site_id) -> dict:
        """Get a single Fuel Station by its site_id."""
        # _LOGGER.debug("get_site_id")
        # _LOGGER.debug(site_id)

        return self.stations[self.stations["site_id"].str.contains(site_id)].to_dict(
            "records"
        )[0]

    def get_stations_options(self) -> list:
        """Return Map of Stations suitable for options selector."""
        df = self.stations.copy()

        df = df.sort_values(by=["brand", "postcode"])

        df["output"] = df["brand"] + ", " + df["address"] + ", " + df["postcode"]

        def map_options(site_id, address):
            return {"label": address, "value": site_id}

        options = map(map_options, df["site_id"].to_list(), df["output"].to_list())

        return list(options)

    async def __open_session(self):
        timeout = aiohttp.ClientTimeout(total=5)
        self.session = aiohttp.ClientSession(
            timeout=timeout,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Cache-Control": "max-age=0",
            },
        )

    async def __close_session(self):
        await self.session.close()


## Example JSON
#
# {
#     "site_id": "gcw9tpts8jzw",
#     "brand": "ESSO",
#     "address": "KEIGHLEY ROAD, HALIFAX",
#     "postcode": "HX2 8BA",
#     "location": {
#         "latitude": 53.743175,
#         "longitude": -1.882085
#     },
#     "prices": {
#         "B7": 146.9,
#         "SDV": 159.9,
#         "E10": 137.9,
#         "E5": 150.9
#     }
# },

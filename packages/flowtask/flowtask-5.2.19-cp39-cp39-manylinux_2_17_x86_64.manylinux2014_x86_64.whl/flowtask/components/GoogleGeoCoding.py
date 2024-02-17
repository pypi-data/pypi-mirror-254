# import orjson
import asyncio
import httpx
import logging
# import requests
import pandas as pd
from flowtask.conf import GOOGLE_API_KEY
from flowtask.components import DtComponent
from flowtask.exceptions import ComponentError


logging.getLogger("httpx").setLevel(logging.WARNING)


class GoogleGeoCoding(DtComponent):
    base_url: str = "https://maps.googleapis.com/maps/api/geocode/json"

    async def start(self, **kwargs):
        if self.previous:
            self.data = self.input
        if not hasattr(self, 'columns'):
            raise RuntimeError(
                'GoogleGeoCoding requires a Column Attribute'
            )
        if not isinstance(self.columns, list):
            raise RuntimeError(
                'GoogleGeoCoding requires a Column Attribute as list'
            )
        if not isinstance(self.data, pd.DataFrame):
            raise ComponentError(
                "Incompatible Pandas Dataframe", code=404
            )
        return True

    async def get_coordinates(self, idx, row):
        # example: 5445 Knoll Creek Drive Apt K, Hazelwood, MO, 63042
        street_address = self.columns[0]
        if pd.notnull(row[street_address]):
            address = ', '.join(row[self.columns])
            params = {
                "address": address,
                "key": GOOGLE_API_KEY
            }
            async with httpx.AsyncClient() as client:
                response = await client.get(self.base_url, params=params)
                if response.status_code == 200:
                    result = response.json()
                    if result['status'] == 'OK':
                        data = result['results'][0]
                        # geometry_str = str(orjson.dumps(data['geometry']).decode('utf-8'))
                        return idx, {
                            # "geometry": geometry_str,
                            "latitude": data['geometry']['location']['lat'],
                            "longitude": data['geometry']['location']['lng'],
                            "formatted_address": data['formatted_address'],
                            "place_id": str(data['place_id'])
                        }
        return idx, None

    async def run(self):
        # initialize columns:
        self.data['geometry'] = pd.NaT
        self.data['place_id'] = pd.NaT
        self.data['formatted_address'] = pd.NaT
        self._result = self.data
        tasks = [
            self.get_coordinates(idx, row) for idx, row in self.data.iterrows()
            if pd.isnull(row.get('place_id', None))
        ]
        results = await asyncio.gather(*tasks)
        for idx, result in results:
            if result:
                for key, value in result.items():
                    self.data.at[idx, key] = value
        return self._result

    async def close(self):
        pass

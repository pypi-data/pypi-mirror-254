import requests
from bustimes import process_data

class Bus:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_bus_stop(self, stop_id: int):
        ''' Gets bus stop info about a specific bus stop.\n
        Args:
            stop_id (int): The bus stop number.
        '''
        
        params = {'apikey': self.api_key}
        headers = {'Accept': 'application/json'}
        bus_data = requests.get(f'https://api.translink.ca/rttiapi/v1/stops/{stop_id}', params=params, headers=headers, timeout=5)
        if bus_data.status_code == 200:
            bus_data = bus_data.json()
            bus_data = process_data.process_bus_stop(bus_data)
            return bus_data
            
    def get_bus_stops_around_location(self,
                                    route: int = None, lat: float = None,
                                    long: float = None, radius: int = 500):
        ''' Gets bus stop info about all bus stops around a specific location.\n
        Args:
            route (int): (Optional) Used to filter stops by bus route.\n
            lat (float): The latitude of the location.\n
            long (float): The longitude of the location.\n
            radius (int): (Optional) The radius around the location to search for bus stops. Default is 500 meters.
        '''   
        params = {'apikey': self.api_key, 'RouteNo':route, 'lat': lat, 'long': long, 'radius': radius}
        headers = {'Accept': 'application/json'}
        bus_data = requests.get('https://api.translink.ca/rttiapi/v1/stops', params=params, headers=headers, timeout=5)
        if bus_data.status_code == 200:
            bus_data = bus_data.json()
            bus_data = process_data.process_multiple_bus_stops(bus_data)
            return bus_data
        else:
            bus_data = bus_data.json()
            if bus_data['Code'] == '10001':
                raise InvalidAPIKeyError('Invalid API Key')
            if bus_data['Code'] == '10002':
                raise DBConnectionError('Database Connection Error')
            if bus_data['Code'] == '1001':
                raise InvalidBusStopError('Invalid Stop Number')
            if bus_data['Code'] == '1002':
                raise InvalidBusStopError('Stop Not Found')
            if bus_data['Code'] == '1011':
                raise InvalidLocationError('Invalid Location')
            if bus_data['Code'] == '1012':
                raise InvalidBusStopError('Stop Not Found')
            if bus_data['Code'] == '1014':
                raise RadiusTooLargeError('Radius Too Large')
            if bus_data['Code'] == '1015':
                raise InvalidBusRouteError('Invalid Route')
            raise UnknownError(bus_data['Message'])

    def get_bus_times(self, stop_id: int, route: str = None, number_of_departures: int = 6):
        ''' Gets bus departure times for a specific bus stop.\n
        Args:
            stop_id (int): The bus stop number.\n
            route (str): (Optional) Used to filter departure times by bus route.\n
            number_of_departures (int): (Optional) The number of departure times to return. Default is 6.
        '''
        params = {'apikey': self.api_key, 'count': number_of_departures}
        if route is not None:
            params.update({'routeNo': route})
        headers = {'Accept': 'application/json'}
        bus_data = requests.get(f'https://api.translink.ca/rttiapi/v1/stops/{stop_id}/estimates', params=params, headers=headers, timeout=5)
        if bus_data.status_code == 200:
            bus_data = bus_data.json()
            bus_data = process_data.process_bus_departure_times(bus_data)
            return bus_data
        bus_data = bus_data.json()
        if bus_data['Code'] == '10001':
            raise InvalidAPIKeyError('Invalid API Key')
        if bus_data['Code'] == '10002':
            raise DBConnectionError('Database Connection Error')
        if bus_data['Code'] == '3001':
            raise InvalidBusStopError('Invalid Stop Number')
        if bus_data['Code'] == '3002':
            raise InvalidBusStopError('Stop Not Found')
        if bus_data['Code'] == '3004':
            raise InvalidBusRouteError('Invalid Route')
        raise UnknownError(bus_data['Message'])

class DBConnectionError(Exception):
    pass

class InvalidAPIKeyError(Exception):
    pass

class InvalidBusStopError(Exception):
    pass

class InvalidBusRouteError(Exception):
    pass

class InvalidLocationError(Exception):
    pass

class RadiusTooLargeError(Exception):
    pass

class UnknownError(Exception):
    pass


import string
import re

def process_bus_stop(bus_data: dict):
    stop_number = int(bus_data['StopNo'])
    stop_name: str = bus_data['Name']
    stop_name = re.sub(r'\bNB\b', 'Northbound', stop_name)
    stop_name = re.sub(r'\bSB\b', 'Southbound', stop_name)
    stop_name = re.sub(r'\bEB\b', 'Eastbound', stop_name)
    stop_name = re.sub(r'\bWB\b', 'Westbound', stop_name)
    stop_name = re.sub(r'\bFS\b', '@', stop_name)
    stop_name = re.sub(r'\bNS\b', '@', stop_name)
    stop_name = re.sub(r'\bSTN\b', 'Station', stop_name)
    stop_name = string.capwords(stop_name, sep=' ')
    bay_number: str = bus_data['BayNo']
    if bay_number == 'N':
        bay_number = None
    else:
        bay_number = int(bay_number)
    at_street: str = bus_data['AtStreet']
    if re.match(r'BAY \d+', at_street):
        at_street = None
    else:
        at_street = string.capwords(at_street, sep=' ')
    routes: str = bus_data['Routes'].lstrip('0')
    return {'StopNumber': stop_number,'StopName': stop_name, 'BayNumber': bay_number, 'AtStreet': at_street, 'Routes': routes}

def process_multiple_bus_stops(bus_data: dict):
    bus_stops = []
    for bus_stop in bus_data:
        bus_stop_data = process_bus_stop(bus_stop)
        if 'Platform' in bus_stop_data['StopName'] or bus_stop_data['StopName'].endswith('New'):
            continue
        bus_stops.append(bus_stop_data)
    return bus_stops

def process_bus_departure_times(bus_data: dict):
    departure_times = {}
    for routes in bus_data:
        route_number_without_leading_zero = routes['RouteNo'].lstrip('0')
        departure_times.update({route_number_without_leading_zero:[]})
        for departure in routes['Schedules']:
            real_time: bool = False
            is_delayed: bool = False
            is_early: bool = False
            destination: str = departure['Destination']
            destination = re.sub(r'\bSTN\b', 'Station', destination)
            destination = re.sub(r'\bEXP\b', 'Express', destination)
            destination = re.sub(r'\bEXCH\b', 'Exchange', destination)
            destination = re.sub(r'\bCTRL\b', 'Central', destination)
            destination = re.sub(r'\bCTR\b', 'Centre', destination)
            destination = string.capwords(destination, sep=' ')
            leave_time: str = departure['ExpectedLeaveTime']
            leave_time = leave_time.split(' ')[0]
            status: str = departure['ScheduleStatus']
            if status == ' ':
                real_time = True
            if status == '-':
                real_time = True
                is_delayed = True
            if status == '+':
                real_time = True
                is_early = True
            if departure['CancelledTrip'] or departure['CancelledStop']:
                cancelled_trip = True
            else:
                cancelled_trip = False
            countdown_time: int = departure['ExpectedCountdown']
            departure_times[route_number_without_leading_zero].append({"RouteNumber": route_number_without_leading_zero, "Destination": destination, "LeaveTime": leave_time, "CountdownTime": countdown_time, "RealTime": real_time, "IsDelayed": is_delayed, "IsEarly": is_early, "CancelledTrip": cancelled_trip})
    return departure_times

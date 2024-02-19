import requests
import json
import datetime
import logging

logger = logging.getLogger(__name__)

class ReadyDecorator:
    
    """ 
    This decorator will allow the use of a method only if the client has been correctly set first 
    When client is set properly, is_ready variable should be set to True
    """
    
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            if instance.is_ready:
                return self.func(instance, *args, **kwargs)
            else:
                raise ValueError("Cannot execute method when is_ready is False.")
        return wrapper

class StravApiClient():
    
    def __init__(self, strava_access_token=None):
        self.is_ready = False
        self.strava_access_token = strava_access_token
        self.api_base_url = "https://www.strava.com/api/v3"
        self.headers = {'Authorization': f'Bearer {strava_access_token}'}
    
    @staticmethod
    def invert_lat_lng(coordinates: list):
        if len(coordinates) != 2: 
            raise Exception("Coordinates must be provided in a list of exactly 2 elements : [latitude, longitude]")
        return [coordinates[1], coordinates[0]]

    @staticmethod
    def convert_to_timestamp(input_date):
        
        if isinstance(input_date, (int, float)):
            # If the input is already a timestamp
            return int(input_date)
        
        if isinstance(input_date, datetime.datetime):
            # If the input is a datetime object
            return input_date.timestamp()
        
        elif isinstance(input_date, datetime.date):
            # If the input is a date, convert it to datetime and then get the timestamp
            date_object = datetime.datetime.combine(input_date, datetime.time.min)
            return int(date_object.timestamp())
    
        elif isinstance(input_date, str):
            # If the input is a string, try parsing it
            try:
                # we try parsing it a first time
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    # we try parsing it a second time
                    date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                except ValueError:
                    # Handle other date formats here if I need
                    raise ValueError("Unsupported date format")            
            return date_object.timestamp()
        else:
            raise ValueError("Unsupported input type")
    
    def set_strava_access_token(self, strava_access_token):
        self.strava_access_token = strava_access_token
        self.headers = {'Authorization': f'Bearer {strava_access_token}'}
    
    def check_if_ready(self):
        if self.strava_access_token is None:
            logger.warning("strava_access_token has not been defined in stravapi_cli")
            self.is_ready = False
            return False
        self.is_ready = True
        return True
    
    @ReadyDecorator
    def get_strava_access_token(self):
        return self.strava_access_token
    
    @ReadyDecorator
    def get_athlete_stats(self, athlete_id):
        athlete_stats_endpoint = f"{self.api_base_url}/athletes/{athlete_id}/stats"
        response = requests.get(
            athlete_stats_endpoint,
            headers = self.headers)
        return response.json()

    @ReadyDecorator
    def get_athlete_activities(self, page='1', per_page='10', start_date=None, end_date=None):
        activities_endpoint = f"{self.api_base_url}/athlete/activities"
        params = {
            'page': page,
            'per_page': per_page
        }
        if start_date: params["after"] = StravApiClient.convert_to_timestamp(start_date)
        if end_date:   params["before"] = StravApiClient.convert_to_timestamp(end_date)
        response = requests.get(
            activities_endpoint,
            headers = self.headers,
            params = params)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"{response.status_code}, {response.text}")
            return f"An error occured while fetching user activities"


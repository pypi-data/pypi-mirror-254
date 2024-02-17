import json
import logging
import os
import time
from datetime import datetime

import requests

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
    
class StravAuthClient():
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_ready = False
        self.required_app_credentials = [
            'client_id', 
            'client_secret', 
            'redirect_uri']
        self._app_credentials = {}
        self.user_oauth_credentials = {
            'access_token': None, 
            'refresh_token': None, 
            'expires_at': None}
        self.athlete_summary = None
        self.strava_oauth_base_endpoint = 'https://www.strava.com/oauth/'
        self.strava_oauth_token_endpoint = f"{self.strava_oauth_base_endpoint}token"
        self.scope="read_all,activity:read_all"

    # ?-------------------------------------------------------------------------------------------
    # ? APP CREDENTIALS
    @ReadyDecorator
    def get_app_credentials(self):
        # Returns the app credentials
        return self._app_credentials
    
    def set_app_credentials(self, client_id, client_secret, redirect_uri):
        # Allows defining manually the required credentials
        self._app_credentials.update({
            'client_id':        client_id,
            'client_secret':    client_secret,
            'redirect_uri':     redirect_uri
        })
    
    def check_app_credentials(self):
        # Will check that any required application credential is well defined
        # If not, will return False and the first missing credential encountered
        for credential in self.required_app_credentials:
            if credential not in self._app_credentials.keys() or self._app_credentials[credential] is None:
                return False, credential
        return True, ''
    
    
    # ?-------------------------------------------------------------------------------------------
    # ? USER OAUTH CREDENTIALS
    @ReadyDecorator
    def get_user_oauth_credentials(self):
        return self.user_oauth_credentials

    @ReadyDecorator
    def set_user_oauth_credentials_from_user(self, user):
        """ 
        Allows to set user oauth credentials from a user passed to the function.
        This user is expected to come with the following attributes:
            - strava_access_token 
            - strava_refresh_token
            - strava_expires_at
        """ 
        self.user_oauth_credentials.update({
            'access_token':  user.strava_access_token, 
            'refresh_token': user.strava_refresh_token, 
            'expires_at':    user.strava_expires_at
        })
    
    
    # ?-------------------------------------------------------------------------------------------
    # ? AUTHORIZATION URL AND CODE
    @ReadyDecorator
    def get_authorization_url(self):
        # Generates authorization URL to redirect user requesting access
        return (
            f"{self.strava_oauth_base_endpoint}authorize?"
            f"client_id={self._app_credentials['client_id']}&"
            f"redirect_uri={self._app_credentials['redirect_uri']}&"
            f"response_type=code&scope={self.scope}")

    @ReadyDecorator
    def exchange_authorization_code(self, authorization_code):
        # Exchange authorization code for a new access token
        # Will set access_token, refresh_token, expires_at
        # Will return the response json formatted or an Exception if an error occured
        data = {
            'client_id':     self._app_credentials['client_id'],
            'client_secret': self._app_credentials['client_secret'],
            'code':          authorization_code,
            'grant_type':    'authorization_code'
        }        
        response = requests.post(self.strava_oauth_token_endpoint, data=data)
        json_response = response.json()
        if response.status_code == 200:      
            self.user_oauth_credentials.update({
                'access_token':  json_response['access_token'],
                'refresh_token': json_response['refresh_token'],
                'expires_at':    json_response['expires_at']
            })
            self.athlete_summary = json_response['athlete']
            return json_response
        else:
            raise Exception(f"Authorization code could not be exchanged: {response.status_code}")
    

    # ?-------------------------------------------------------------------------------------------
    # ? ACCESS AND REFRESH TOKENS
    @ReadyDecorator
    def is_access_token_valid(self):
        # Checks if expires_at date is to come or already past, 
        # to know if access_token needs to be refreshed with the help of refresh_token
        expires_at = self.user_oauth_credentials['expires_at']
        if isinstance(expires_at, datetime):
            expires_at = expires_at.timestamp()
        if not expires_at or time.time() > expires_at:
            logger.warning("Access Token has expired, it has to be renewed with the last known refresh token.")
            return False
        else: 
            logger.info("Access Token is still valid and can be used.")
            return True

    @ReadyDecorator
    def refresh_that_access_token(self):
        # Get a new access token with the given refresh_token
        # Returns 4 things: new access_token, (maybe new) refresh_token, new expires_at, and the response (json formatted)
        data = {
            'client_id':     self._app_credentials['client_id'],
            'client_secret': self._app_credentials['client_secret'],
            'refresh_token': self.user_oauth_credentials['refresh_token'],
            'grant_type':    'refresh_token'
        }
        response = requests.post(self.strava_oauth_token_endpoint, data=data)
        json_response = response.json()
        if response.status_code == 200:
            self.user_oauth_credentials.update({
                'access_token':  json_response['access_token'],
                'refresh_token': json_response['refresh_token'],
                'expires_at':    json_response['expires_at']
            })
            logger.info("Success: access_token has been refreshed")
        else:
            logger.error("Access token could not be refreshed", response)
            raise Exception(f"Access token could not be refreshed: {response}")
    
    
    # ?-------------------------------------------------------------------------------------------
    @ReadyDecorator
    def get_athlete_summary(self):
        return self.athlete_summary
    
    def check_if_ready(self):
        """
        Client is considered ready if:
            - all _app_credentials have been set
            - ?
        """
        credentials_ok, missing_credential = self.check_app_credentials()
        if not credentials_ok:
            self.is_ready = False # in case it had been set to True before
            error_msg = f"{missing_credential} is a required credential and is missing in the credentials dict"
            logger.error(error_msg)
            raise Exception(error_msg)        
        self.is_ready = True
        return True

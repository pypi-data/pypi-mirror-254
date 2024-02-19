import unittest
from datetime import datetime, timedelta
from unittest.mock import patch
from clients.stravauth_cli import StravAuthClient

class TestStravAuthClient(unittest.TestCase):
    
    def setUp(self):
        # Initialisation pour chaque test
        self.client = StravAuthClient()
        self.client.set_app_credentials('your_client_id', 'your_client_secret', 'your_redirect_uri')
        self.client.check_if_ready()
        
    def test_check_app_credentials(self):
        # Teste si la méthode détecte correctement les informations d'identification manquantes
        self.assertTrue(self.client.check_app_credentials())

        # Simule l'absence d'une information d'identification
        for required_credential in self.client.required_app_credentials:
            old_credential_val = self.client._app_credentials[required_credential]
            self.client._app_credentials[required_credential] = None
            self.assertFalse(self.client.check_app_credentials()[0])
            self.client._app_credentials[required_credential] = old_credential_val
    
    def test_exchange_authorization_code(self):
        # Teste si la méthode échange correctement le code d'autorisation
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {
                'access_token': 'new_access_token',
                'refresh_token': 'new_refresh_token',
                'expires_at': int((datetime.now() + timedelta(hours=1)).timestamp()),
                'athlete': 'athlete_summary'
            }

            authorization_code = 'authorization_code'
            response = self.client.exchange_authorization_code(authorization_code)

            self.assertEqual(response['access_token'], 'new_access_token')
            self.assertEqual(response['refresh_token'], 'new_refresh_token')

            # Vérifie si les attributs de l'instance ont été mis à jour correctement
            self.assertEqual(self.client.user_oauth_credentials['access_token'], 'new_access_token')
            self.assertEqual(self.client.user_oauth_credentials['refresh_token'], 'new_refresh_token')  
            self.assertEqual(self.client.user_oauth_credentials['expires_at'], int((datetime.now() + timedelta(hours=1)).timestamp()))      


if __name__ == '__main__':
    unittest.main()
    
    
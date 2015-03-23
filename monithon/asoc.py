from requests import HTTPError

from social.exceptions import AuthFailed

from social.backends.oauth import BaseOAuth2



class AsocOauth2(BaseOAuth2):
    name = 'asoc'
    AUTHORIZATION_URL = 'http://www.ascuoladiopencoesione.it/oauth/authorize'
    ACCESS_TOKEN_URL = 'http://www.ascuoladiopencoesione.it/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_id(self, details, response):
        return response.get('ID')

    def get_user_details(self, response):
        """Return user details from Instagram account"""
        username = response.get('user_nicename')
        firstname = response.get("user_nicename")
        email = response.get('user_email', '')
        uid = response.get("ID")
        return {'username': username,
                "first_name": firstname,
                "id":uid,
                'email': email}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('http://www.ascuoladiopencoesione.it/oauth/me',
                             params={'access_token': access_token})
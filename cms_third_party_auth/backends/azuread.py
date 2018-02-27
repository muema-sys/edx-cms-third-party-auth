try:
    from social.backends.azuread import AzureADOAuth2 as BaseAzureADOAuth2
except ImportError:
    from social_core.backends.azuread import AzureADOAuth2 as BaseAzureADOAuth2


class AzureADOAuth2(BaseAzureADOAuth2):

    def get_user_id(self, details, response):
        """Use upn as unique id"""
        return response.get('unique_name')

    def get_user_details(self, response):
        """Return user details from Azure AD account"""
        fullname, first_name, last_name = (
            response.get('name', ''),
            response.get('given_name', ''),
            response.get('family_name', '')
        )
        return {'username': fullname,
                'email': response.get('email', response.get('unique_name')),
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

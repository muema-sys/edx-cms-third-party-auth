edx-cms-third-party-auth

Integrating Third Party Authentication in Open edX Studio

Install (*only for Open edX Ficus & Ginkgo Releases):

pip install -e git+https://github.com/raccoongang/edx-cms-third-party-auth.git@master#egg=edx_cms_third_party_auth

In the edx/app/edxapp/cms.env.json file, edit the file so that it includes the following lines in the features section.

.........
"FEATURES" : {
    ...
    "ENABLE_COMBINED_LOGIN_REGISTRATION": true,
    "ENABLE_THIRD_PARTY_AUTH": true
}
.........

In the edx-platform/cms/startup.py file, edit the define "run" so that includes the following lines in it.

.........
# To override the settings before executing the autostartup() for python-social-auth
    if settings.FEATURES.get('ENABLE_THIRD_PARTY_AUTH', False):
       enable_third_party_auth()
.........

Also in the end of edx-platform/cms/startup.py file add the following function definition.

.........
def enable_third_party_auth():
    """
    Enable the use of third_party_auth, which allows users to sign in to edX
    using other identity providers. For configuration details, see
    common/djangoapps/third_party_auth/settings.py.
    """

    from third_party_auth import settings as auth_settings
    from cms_third_party_auth.settings import add_locale_path

    auth_settings.apply_settings(settings)
    add_locale_path()
.........

In the beggining of edx-platform/cms/urls.py file, add the following url (right after url(r'', include('student.urls'))).

.........
url(r'', include('cms_third_party_auth.urls')),
.........


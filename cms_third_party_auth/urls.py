from django.conf import settings
from django.conf.urls import url, include

from views import course


urlpatterns = (
    url(r'^login$', 'contentstore.views.login_page'),
    url(r'^register', 'contentstore.views.signup'),
    url(r'^course/$', course),
)

if settings.FEATURES.get('ENABLE_THIRD_PARTY_AUTH'):
    urlpatterns += (
        url(r'', include('third_party_auth.urls')),
        url(r'api/third_party_auth/', include('third_party_auth.api.urls')),
        # NOTE: The following login_oauth_token endpoint is DEPRECATED.
        # Please use the exchange_access_token endpoint instead.
        url(r'^login_oauth_token/(?P<backend>[^/]+)/$', 'student.views.login_oauth_token'),
    )

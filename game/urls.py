from django.conf.urls import url
from .views import log_in, log_out, sign_up, homeView,get_match_score


urlpatterns = [
    url(r'^$', homeView, name='homeView'),
    # url(r'^home/$', main, name='main'),
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^score/$', get_match_score, name='score'),
]

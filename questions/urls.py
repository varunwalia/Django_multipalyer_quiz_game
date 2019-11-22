from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from questions import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^question/(?P<id>\d+)/$', views.one_question, name='question_single'),
    url(r'^question/$', views.home, name='question_home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
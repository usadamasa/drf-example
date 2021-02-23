from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views as quickstart_views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('tutorial.quickstart.urls')),
    path('', include('tutorial.snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views as quickstart_views

router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('tutorial.snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

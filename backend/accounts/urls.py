from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter

from checker.views import LinkViewSet

app_name = 'checker'

router = DefaultRouter()
router.register('', LinkViewSet, basename='checker')

urlpatterns = router.urls

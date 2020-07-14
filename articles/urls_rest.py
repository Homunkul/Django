from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet,TagViewSet, CommentaryViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='аrticle')
urlpatterns = router.urls

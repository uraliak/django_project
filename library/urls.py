from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import (
    AuthorViewSet,
    BookViewSet,
    LibraryViewSet,
    PublisherViewSet,
    ReviewViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="author")
router.register(r"publishers", PublisherViewSet, basename="publisher")
router.register(r"libraries", LibraryViewSet, basename="library")
router.register(r"books", BookViewSet, basename="book")
router.register(r"users", UserViewSet, basename="user")
router.register(r"reviews", ReviewViewSet, basename="review")

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

from django.urls import path
from ninja import NinjaAPI
from .api.license_api import license_router
from .api.user_api import user_router

api = NinjaAPI()

api.add_router("/licenses", license_router)
api.add_router("/users", user_router)

urlpatterns = [
    path("api/", api.urls),
]

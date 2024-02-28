from django.urls import path
from ninja import NinjaAPI
from .api.license_api import license_router
from .api.user_api import user_router
from .api.chassis_api import chassis_router
from .api.aptica_api import aptica_router
from .api.element_api import element_router
from .api.component_api import component_router

api = NinjaAPI()

api.add_router("/licenses", license_router)
api.add_router("/users", user_router)
api.add_router("/chassis", chassis_router)
api.add_router("/aptica", aptica_router)
api.add_router("/elements", element_router)
api.add_router("/components", component_router)

urlpatterns = [
    path("api/", api.urls),
]

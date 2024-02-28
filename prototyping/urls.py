from django.urls import path
from ninja import NinjaAPI
from .router.license_route import license_router
from .router.user_route import user_router
from .router.chassis_route import chassis_router
from .router.aptica_route import aptica_router
from .router.element_route import element_router
from .router.component_route import component_router
from .router.client_route import client_router

api = NinjaAPI()

api.add_router("/licenses", license_router)
api.add_router("/users", user_router)
api.add_router("/chassis", chassis_router)
api.add_router("/aptica", aptica_router)
api.add_router("/elements", element_router)
api.add_router("/components", component_router)
api.add_router("/clients", client_router)

urlpatterns = [
    path("api/", api.urls),
]

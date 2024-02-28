from django.urls import path
from ninja import NinjaAPI
from .router.license_route import license_router
from .router.user_route import user_router
from .router.chassis_route import chassis_router
from .router.aptica_route import aptica_router
from .router.element_route import element_router
from .router.component_route import component_router
from .router.client_route import client_router
from .router.project_route import project_router
from .router.message_route import message_router
from .router.release_route import release_router 

api = NinjaAPI()

api.add_router("/licenses", license_router)
api.add_router("/users", user_router)
api.add_router("/chassis", chassis_router)
api.add_router("/aptics", aptica_router)
api.add_router("/elements", element_router)
api.add_router("/components", component_router)
api.add_router("/clients", client_router)
api.add_router("/projects", project_router)
api.add_router("/messages", message_router)
api.add_router("/releases", release_router)

urlpatterns = [
    path("api/", api.urls),
]

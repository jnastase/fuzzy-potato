from django.urls import path, include

from . import views
from common.api import router

urlpatterns = [
    # path("", views.index, name="index"),
    path("", include(router.urls)),
]

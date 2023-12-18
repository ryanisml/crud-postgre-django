from django.contrib import admin
from django.urls import path, include
from employee_api.router import router

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
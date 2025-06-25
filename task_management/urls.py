from django.contrib import admin
from users.views import home
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('tasks/', include("tasks.urls")),
]

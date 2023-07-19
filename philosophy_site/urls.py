from django.contrib import admin
from django.urls import include, path
from philo_group import views as philoViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('philo_group.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

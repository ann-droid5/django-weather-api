from django.contrib import admin
from django.urls import path, include

from accounts.views import login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/weather/', include('weather.urls')),
    #path('api/', include('accounts.urls')),
    path('', login_page, name='login'),
    path('', include('accounts.urls')),  # instead of 'api/'

]

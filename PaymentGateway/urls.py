from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('home/', Home, name='home'),
    path('success/', success, name='Success'),
    path('failure/', failure, name='Failure'),
]

# url(r'^admin/', include(admin.site.urls)),
# url(r'^home/',Home),
# url(r'^Success/',success),
# url(r'^Failure/',failure),
# from django.urls import path
# from .views import *


# urlpatterns = [
#     path('', index, name='home'),
#     # path('home/', Home, name='home'),
#     # path('success/', success, name='Success'),
#     # path('failure/', failure, name='Failure'),
# ]

# url(r'^admin/', include(admin.site.urls)),
# url(r'^home/',Home),
# url(r'^Success/',success),
# url(r'^Failure/',failure),


from django.urls import path
from .views import home, payu_checkout, payu_failure, payu_success


urlpatterns = [
    path('', home, name="home"),
    path('payu_checkout', payu_checkout, name="payu_checkout"),
    path('payu/failure', payu_failure, name="payu_failure"),
    path('payu/success', payu_success, name="payu_success"),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('', index_page, name='index_page'),
    path('bands/', band_list, name='band_list'),
    path('bands/<int:band_id>/', band_detail, name='band_detail'),
    path('sign-up/', sign_up, name='sign_up'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    # TnC
    path('privacy/', privacy_policy_view, name='privacy_policy'),
    path('terms/', terms_of_service_view, name='terms_of_service'),

]
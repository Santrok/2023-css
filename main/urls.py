from django.urls import path

from main.views import get_page, page_add_car, detail_info, get_brand, search, registration, login_user, logout_user, \
    kabinet

urlpatterns = [
    path('', get_page, name='home'),
    path('add_car/', page_add_car, name='add_car'),
    path('detail/<int:id>/', detail_info, name='detail_info'),
    path('brand/', get_brand, name='brand'),
    path('search/', search, name='search'),
    path('registration/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('kabinet/', kabinet, name='kabinet'),
]
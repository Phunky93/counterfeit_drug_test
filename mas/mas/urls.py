"""mas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mas_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',show_index),
    url(r'^show_index', show_index, name="show_index"),
    url(r'^check_login', check_login, name="check_login"),
    url(r'^logout',logout,name="logout"),
    url(r'^register',register,name="register"),
    ##########login end

    ################Admin start
    url(r'^show_home_admin',show_home_admin,name="show_home_admin"),
    url(r'^show_request_admin',show_request_admin,name="show_request_admin"),
    url(r'^approve',approve,name="approve"),
    url(r'^reject',reject,name="reject"),
    url(r'^display_view_customers',display_view_customers,name="display_view_customers"),
    url(r'^display_view_pharmacys',display_view_pharmacys,name="display_view_pharmacys"),
    url(r'^display_view_distributors',display_view_distributors,name="display_view_distributors"),
    url(r'^display_view_manufacturers',display_view_manufacturers,name="display_view_manufacturers"),
    url(r'^show_home_manufacturer',show_home_manufacturer,name="show_home_manufacturer"),
    url(r'^show_home_distributor',show_home_distributor,name="show_home_distributor"),
    url(r'^show_home_pharmacy',show_home_pharmacy,name="show_home_pharmacy"),
    url(r'^display_add_medicine',display_add_medicine,name="display_add_medicine"),
    url(r'^add_medicine',add_medicine,name="add_medicine"),
    url(r'^display_view_medicine',display_view_medicine,name="display_view_medicine"),
    url(r'^get_medicine_request_dis',get_medicine_request_dis,name="get_medicine_request_dis"),
    url(r'^get_collected_medicine_dis',get_collected_medicine_dis,name="get_collected_medicine_dis"),
    url(r'^collect_med_dis',collect_med_dis,name="collect_med_dis"),
    url(r'^distribute',distribute,name="distribute"),
    url(r'^display_medicine_stock_pharmacy',display_medicine_stock_pharmacy,name="display_medicine_stock_pharmacy"),

    url(r'^customer_register',customer_register,name="customer_register"),
    url(r'^find_login',find_login,name="find_login"),
    url(r'^get_info',get_info,name="get_info"),
    url(r'^do_payment',do_payment,name="do_payment"),
]

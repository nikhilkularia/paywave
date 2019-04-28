from django.urls import path

from . import views

urlpatterns = [
    path('mobile/',views.mobile,name="mobile"),
    path('dthcard/',views.dthcard,name="dthcard"),
    path('electricity/',views.electricity,name="electricity"),
    path('movie/',views.movie,name="movie"),
    path('gas/',views.gas,name="gas"),
    path('actmobile/',views.actmobile,name="actmobile"),
    path('payment/',views.payment,name="payment"),
    path('final/',views.final,name="final"),
    path('actdth/',views.actdth,name="actdth"),
    path('credit_payment/',views.credit_payment,name="creditpayment"),
    path('actelectricity/',views.actelectricity,name='actelectricity'),
    path('actgas/',views.actgas,name='actgas'),
    path('datacard/',views.datacard,name="datacard"),
    path('actdatacard/',views.actdatacard,name="actdatacard"),
    path('water/',views.water,name='water'),
    path('actwater/',views.actwater,name='actwater'),
    path('landline/', views.landline, name='landline'),
    path('actlandline/', views.actlandline, name='actladline'),
    path('broadband/', views.broadband, name='broadband'),
    path('actbroadband/', views.actbroadband, name='actbroadband'),
    path('metro/', views.metro, name='metro'),
    path('actmetro/', views.actmetro, name='actmetro'),
    path('mobile_detail/',views.mobile_detail,name='mobiledetail'),
    path('dth_detail/',views.dth_detail,name='dthdetail'),
    path('elec_detail/', views.elec_detail, name='elecdetail'),
    path('gas_detail/', views.gas_detail, name='gasdetail'),
    path('land_detail/',views.land_detail,name='landdetail'),
    path('water_detail/',views.water_detail,name='waterdetail'),
    path('datacard_detail/',views.datacard_detail,name='datacarddetail'),
    path('broad_detail/',views.broad_detail,name='broaddetail'),
    path('metro_detail/',views.metro_detail,name='metrodetail')
]

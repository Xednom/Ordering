from django.conf.urls import  url
from ordering import views
from django.contrib.auth.views import(
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    # /ordering/
    url(r'^$', views.home, name='home'),

    url(r'^detail/$', views.detail, name='detail'),

    url(r'^inventory-menu/$', views.inventory_menu, name='inventory_menu'),

    url(r'^inventory-detail/(?P<inventory_id>[0-9]+)/$', views.inventory_detail, name='inventory_detail'),

    url(r'^inventory-add/$', views.inventory_create, name='inventory_create'),

    url(r'^inventory_delete/(?P<inventory_id>[0-9]+)/$', views.inventory_delete, name='inventory_delete'),

    url(r'^dropship-add/$', views.order_create, name='order_create'),

    url(r'^dropship-edit/(?P<pk>\d+)$', views.order_update, name='order_update'),

    url(r'^dropship-delete/(?P<order_id>[0-9]+)/$', views.order_delete, name='order_delete'),

    url(r'^order-successful/$', views.order_success, name='order_success'),

    url(r'^order-history/(?P<order_id>[0-9]+)/$', views.order_history, name='order_history'),

    url(r'^login/$', login, {'template_name': 'ordering/login_user.html'}, name='login'),

    url(r'^logout/$', logout, {'template_name': 'ordering/logout_user.html'}, name ='logout'),

    url(r'^register/$', views.register, name='register'),

    url(r'^register-sucess/$', views.register_success, name='register_success'),

    url(r'^profile/$', views.view_profile, name='view_profile'),

    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^change-password/$', views.change_password, name='change_password'),

    url(r'^reset-password/$', password_reset, {'template_name': 'ordering/reset_password.html', 'post_reset_redirect': 'ordering:password_reset_done', 'email_template_name': 'ordering/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'ordering/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'ordering/reset_password_confirm.html', 'post_reset_redirect': 'ordering:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'ordering/reset_password_complete.html'}, name='password_reset_complete')
]

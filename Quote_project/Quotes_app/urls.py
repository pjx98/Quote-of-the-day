from django.urls import path
from . import views

from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url


urlpatterns = [
    
    path('', views.today_quote, name="Daily_quote"),
    path('all_quotes/', views.show_all_items, name="all_quotes"),
    path('submit_quote/', views.user_add_quote, name="add_quote"),
    path('subscribe/', views.insert_user_email, name="subscribe")
    
]




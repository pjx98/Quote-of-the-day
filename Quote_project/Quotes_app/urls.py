from django.urls import path
from . import views

from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url


urlpatterns = [
    
    path('', views.today_quote, name="Daily_quote"),
    path('all_quotes/', views.show_all_items, name="show_all"),
    path('submit_quote/', views.user_add_quote, name="add_quote")
    
]




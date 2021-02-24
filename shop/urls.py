from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('prod/', views.prod, name="prod"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('register/', views.register, name="register"),
    path('authenticate/', views.authenticate, name="authenticate"),
    path('logout/', views.logout, name="logout"),
    path('add_product/', views.add_product, name="add_product"),
    path('sell/', views.sell, name="sell"),
]
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("collections/",views.Collections,name='collections'),
    path("collectionsview/<str:name>",views.Collectionsview,name='collectionsview'),
    path("productdetailview/<str:cname>/<str:pname>",views.Productdetailview,name='productdetailview'),
    path("login/",views.login_page,name='login'),
    path("logout/",views.logout_page,name='logout'),
    path("addtocart",views.addtocart,name='addtocart'),
    path("Cart/",views.cart,name='cart'),
    path("delete/<str:cid>",views.delete,name='delete'),

    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about'),




]

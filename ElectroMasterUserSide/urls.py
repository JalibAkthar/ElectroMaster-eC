from django.urls import path
from ElectroMasterUserSide import views

urlpatterns = [
    path('home_page/',views.home_page,name="home_page"),
    path('products_page/',views.products_page,name="products_page"),
    path('single_product/<int:proid>/',views.single_product,name="single_product"),
    path('product_filtered/<cat_name>/',views.product_filtered,name="product_filtered"),

    path('about_us/',views.about_us,name="about_us"),
    path('services/',views.services,name="services"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('save_contact/',views.save_contact,name="save_contact"),

    path('',views.login,name="login"),
    path('signup_save/',views.signup_save,name="signup_save"),
    path('User_Login/',views.User_Login,name="User_Login"),
    path('User_Logout/',views.User_Logout,name="User_Logout"),

    path('cart_page/',views.cart_page,name="cart_page"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('delete_cart/<int:dataid>',views.delete_cart,name="delete_cart"),
    path('check_out/',views.check_out,name="check_out"),
]
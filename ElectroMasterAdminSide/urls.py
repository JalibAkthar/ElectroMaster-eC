from django.urls import path
from ElectroMasterAdminSide import views

urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),

    path('category_page/',views.category_page,name="category_page"),
    path('save_category/',views.save_category,name="save_category"),
    path('category_display/',views.category_display,name="category_display"),
    path('category_edit/<int:dataid>/',views.category_edit,name="category_edit"),
    path('category_update/<int:dataid>/',views.category_update,name="category_update"),
    path('category_delete/<int:dataid>/',views.category_delete,name="category_delete"),

    path('product_page/',views.product_page,name="product_page"),
    path('product_save/',views.product_save,name="product_save"),
    path('product_display/',views.product_display,name="product_display"),
    path('product_edit/<int:dataid>/',views.product_edit,name="product_edit"),
    path('product_update/<int:dataid>/',views.product_update,name="product_update"),
    path('product_delete/<int:dataid>/',views.product_delete,name="product_delete"),

    path('',views.admin_login,name="admin_login"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('display_contact/',views.display_contact,name="display_contact"),
]
from django.urls import path

from .views import productlistview, supplierlistview, addsupplier, addproduct, \
    deleteproduct, confirmdeleteproduct, deletesupplier, confirmdeletesupplier, edit_product_get, edit_product_post, \
    edit_supplier_get, edit_supplier_post, searchsuppliers, products_filtered, loginview, login_action, logout_action, \
    customerlistview, addcustomer, deletecustomer, confirmdeletecustomer, edit_customer_get, edit_customer_post, \
    carlistview, addcar, deletecar, confirmdeletecar, cars_filtered

urlpatterns = [
    
    # #Landing page after login
    # path('landing/', landingview),

    #Loginview and authentication method
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),
    
    # path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('products-by-supplier/<int:id>/', products_filtered),
     path('edit-product-get/<int:id>/', edit_product_get),
     path('edit-product-post/<int:id>/', edit_product_post), 
    

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post), 
    path('search-suppliers/', searchsuppliers),

    # Customer url´s
    path('customers/', customerlistview),
    path('add-customer/', addcustomer),
    path('delete-customer/<int:id>/', deletecustomer),
    path('confirm-delete-customer/<int:id>/', confirmdeletecustomer),
    path('edit-customer-get/<int:id>/', edit_customer_get),
    path('edit-customer-post/<int:id>/', edit_customer_post), 

    # Car url´s
    path('cars/', carlistview),
    path('add-car/', addcar),
    path('delete-car/<int:id>/', deletecar),
    path('confirm-delete-car/<int:id>/', confirmdeletecar),
    path('cars-by-supplier/<int:id>/', cars_filtered),
]
        

from django.urls import path
from .views import ProductView,ProductDelete

urlpatterns = [
    path('product/', ProductView.as_view(), name='products'),
    path('delete/<int:id>/', ProductDelete.as_view(), name='deleteproducts'),

]
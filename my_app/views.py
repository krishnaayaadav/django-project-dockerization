from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product
from django.views import View

class ProductView(View):
    def get(self, request):
        form = ProductForm()
        products = Product.objects.all()
        context = {
            'form': form,
            'prodcuts': products
        }
        return render(request, 'my_app/productform.html', context)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        products = Product.objects.all()
        context = {
            'form': form,
            'prodcuts': products
        }
        return render(request, 'my_app/productform.html', context)

class ProductDelete(View):
    def get(self, request, id):

        try:
            prod = Product.objects.get(pk=id)
        except:
            error = 'Product Does Not Found'
        else:
            prod.delete()
            return redirect('products')
            


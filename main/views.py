from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406355893',
        'name': request.user.username,
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'rating': product.rating,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]
    
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'rating': product.rating,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True, "message": "Registrasi berhasil!"})
            messages.success(request, "Your account has been successfully created!")
            return redirect('main:login')
        else:
            # Ambil semua error menjadi string
            errors = []
            for field, errs in form.errors.items():
                for err in errs:
                    if field != "__all__":
                        errors.append(f"{field.title()}: {err}")
                    else:
                        errors.append(err)
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "errors": errors})
    context = {"form": form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    response = redirect('main:login')
    response.delete_cookie('last_login')
    
    # Tambahkan message untuk toast
    messages.success(request, "You have been successfully logged out!")
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product':product,
    }

    return render(request, "edit_product.html", context)

@require_POST
@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return JsonResponse({"status": "success", "message": "Product deleted successfully"})


@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    # Ambil data dari request POST
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    stock = request.POST.get("stock")
    rating = request.POST.get("rating")
    user = request.user if request.user.is_authenticated else None

    # Validasi sederhana
    if not all([name, price, description, category]):
        return JsonResponse({"error": "Missing required fields"}, status=400)

    # Buat entri produk baru
    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        stock=stock if stock else 0,
        rating=rating if rating else 0,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.category = request.POST.get("category")
        product.stock = request.POST.get("stock")
        product.thumbnail = request.POST.get("thumbnail")
        product.rating = float(request.POST.get('rating', product.rating))
        product.save()
        return JsonResponse({"status": "success", "message": "Product updated successfully!"})
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@csrf_exempt
@require_POST
def delete_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)

        # Optional: pastikan hanya pemilik produk yang bisa hapus
        if product.user != request.user:
            return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

        product.delete()
        return JsonResponse({"status": "success", "message": "Product deleted successfully!"})
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
# ti4
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
# ti6
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406406780',
        'name': 'Farrel Rifqi Bagaskoro',
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "create_product.html", context)

@login_required(login_url='/login') # ti4
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_details.html", context)

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
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
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
    """Return a JSON representation of a single product by id."""
    try:
        product_obj = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product_obj.id),
            'name': product_obj.name,
            'price': product_obj.price,
            'description': product_obj.description,
            'category': product_obj.category,
            'thumbnail': product_obj.thumbnail,
            'is_featured': product_obj.is_featured,
            'user_id': product_obj.user.id if product_obj.user else None,
            'user_username': product_obj.user.username if product_obj.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
# ti4
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # If it's an AJAX request, respond with JSON so client can redirect
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect': reverse('main:login')})
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')

        # invalid form on AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            errors = {field: errors for field, errors in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # set last_login cookie for non-AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect': reverse('main:show_main')})
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

        # invalid form
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            errors = {field: errors for field, errors in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    """Handle both AJAX and regular logout requests."""
    logout(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response = JsonResponse({'success': True, 'redirect': reverse('main:login')})
        response.delete_cookie('last_login')
        return response
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    """Delete a product. Returns JSON for AJAX requests, redirects for normal requests."""
    product = get_object_or_404(Product, pk=id)
    
    # Only owner can delete
    if product.user and request.user != product.user:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'detail': 'Forbidden'}, status=403)
        return HttpResponseRedirect(reverse('main:show_main'))

    product.delete()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'success': True})
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    # ensure price is integer (0 if error)
    try:
        price = int(request.POST.get("price", 0))
    except (TypeError, ValueError):
        price = 0
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


@csrf_exempt
@require_POST
def update_product_entry_ajax(request):
    """AJAX endpoint to update an existing product.

    Expects a POST with 'product_id' and the same fields as create.
    """
    product_id = request.POST.get('product_id')
    if not product_id:
        return HttpResponse(b'Missing product_id', status=400)

    try:
        product_obj = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse(b'Not found', status=404)

    # Only the owner may update (if product has a user)
    if product_obj.user and request.user != product_obj.user:
        return HttpResponse(b'Forbidden', status=403)

    # Update fields (coerce price to int)
    product_obj.name = request.POST.get('name', product_obj.name)
    try:
        product_obj.price = int(request.POST.get('price', product_obj.price))
    except (TypeError, ValueError):
        pass
    product_obj.description = request.POST.get('description', product_obj.description)
    product_obj.category = request.POST.get('category', product_obj.category)
    product_obj.thumbnail = request.POST.get('thumbnail', product_obj.thumbnail)
    product_obj.is_featured = request.POST.get('is_featured') == 'on'

    product_obj.save()

    return HttpResponse(b'OK', status=200)
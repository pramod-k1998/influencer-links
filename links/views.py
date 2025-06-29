
from .models import ProductLink,Category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from .forms import ProductLinkForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# def link_list(request):
#     """
#     Display all product links to any user.
#     Admins will also see edit/delete options.
#     """
#     links = ProductLink.objects.all()
#     return render(request,'links/link_list.html', {'links': links})
def link_list(request):
    selected_category = request.GET.get('category')

    if selected_category:
        links = ProductLink.objects.filter(category__name=selected_category)
    else:
        links = ProductLink.objects.all()

    paginator = Paginator(links, 6)  # 5 links per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, 'links/link_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': selected_category,
    })

def superuser_login_view(request):
    """
    Authenticates superusers using username and password.
    Redirects to link list on success.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("link_list")
        else:
            messages.error(request, "Invalid credentials or not a superuser.")
    return render(request, "links/login.html")

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_superuser)(view_func)

def is_superuser(user):
    return user.is_superuser

@superuser_required
def add_link(request):
    """
    Allows superuser to add a new product link.
    """
    form = ProductLinkForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("link_list")
    return render(request, "links/form.html", {"form": form, "form_title": "Add New Link"})

@superuser_required
def edit_link(request, pk):
    """
    Allows superuser to edit an existing product link.
    """
    link = get_object_or_404(ProductLink, pk=pk)
    form = ProductLinkForm(request.POST or None, instance=link)
    if form.is_valid():
        form.save()  # ✅ saves changes
        return redirect("link_list")
    return render(request, "links/form.html", {"form": form, "form_title": "Edit Link"})

@superuser_required
def delete_link(request, pk):
    """
    Allows superuser to delete an existing product link.
    """
    link = get_object_or_404(ProductLink, pk=pk)
    if request.method == "POST":
        link.delete()
        return redirect("link_list")
    return render(request, "links/confirm_delete.html", {"link": link})


def logout_view(request):
    """
    Logs out the current user and redirects to home.
    """
    logout(request)
    return redirect('link_list')
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book, Category
from .forms import BookForm, CategoryForm

# Create your views here.

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect('/')
    template = 'pages/delete.html'
    return render(request, template)

def update(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book_save = BookForm(request.POST, request.FILES, instance=book)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        obj = BookForm(instance=book)

    template = 'pages/update.html'
    context = {
        'form': obj,
    }
    return render(request, template, context)

def books(request):
    obj = Book.objects.all()
    categorys = Category.objects.all()

    # Search method
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            obj = obj.filter(title__icontains = title)

    form_category = CategoryForm()
    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return redirect('/')
            

    template = 'pages/books.html'
    context = {
        'categorys': categorys,
        'books': obj,
        'form_category': form_category,
    }
    return render(request, template, context)

def home(request):
    obj = Book.objects.all()
    all_books = Book.objects.filter(active=True).count()
    sold_books = Book.objects.filter(status="sold").count()
    rental_books = Book.objects.filter(status="rental").count()
    available_books = Book.objects.filter(status="available").count()
    categorys = Category.objects.all()
    form = BookForm()
    if request.method == 'POST':
        obj = BookForm(request.POST, request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('/')

    form_category = CategoryForm()
    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return redirect('/')

    total_price = 0        
    for book in obj:
        if book.price != None:
            if book.status == "sold":
                sol_price = book.price
                total_price += sol_price

        if book.total_rental != None:
            if book.status == "rental":
                rental_price = book.total_rental
                total_price += rental_price
                
                

    template = 'pages/index.html'
    context = {
        'categorys': categorys,
        'books': obj,
        'form':form,
        'form_category': form_category,
        'all_books': all_books,
        'sold_books': sold_books,
        'rental_books': rental_books,
        'available_books': available_books,
        'total_price': total_price,
        'sol_price': sol_price,
        'rental_price': rental_price,
        

    }
    return render(request, template, context)


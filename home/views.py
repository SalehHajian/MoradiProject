from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.db.models import Q
from cart.models import *


# Create your views here.
def home(request) :
    category = Category.objects.filter(sub_cat=False)
    return render(request , 'home/home.html' , {'category' :category })

def all_product(request , slug=None , id=None):
    products = Product.objects.filter()
    form = SearchForm()
    category = Category.objects.filter(sub_cat=False)
    if slug and id:
        data = get_object_or_404(Category , slug = slug , id = id)
        products = products.filter(category = data)
    return render(request, 'home/product.html' , {'products' : products , 'category' :category , 'form':form})

def product_detail(request , id) :
    product = get_object_or_404(Product , id=id)
    images = Images.objects.filter(product_id = id)
    cart_form = CartForm()
    comment_form = CommentForm()
    reply_form = ReplyForm()
    comment = Comment.objects.filter(product_id=id  , is_reply=False)
    similar = product.tags.similar_objects()[:2]
    is_like = False
    if product.like.filter(id = request.user.id).exists() :
        is_like = True

    is_unlike = False
    if product.unlike.filter(id=request.user.id).exists():
        is_unlike = True

    if product.status != 'None' :
        if request.method == 'POST' :
            variant = Variants.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
            variants = Variants.objects.get(id = var_id)
        else :
            variant = Variants.objects.filter(product_variant_id=id)
            variants = Variants.objects.get(id=variant[0].id)
        context = {'product' : product, 'variants' :variants , 'variant' :variant ,'similar':similar ,
                   'is_like':is_like , 'comment_form':comment_form , 'comment':comment , 'reply_form':reply_form , 'is_unlike':is_unlike , 'images':images , 'cart_form':cart_form}
        return render(request , 'home/detail.html' , context)
    else :
        return render(request ,'home/detail.html' , {'product' : product,'similar':similar , 'is_like':is_like , 'comment_form':comment_form , 'comment':comment , 'reply_form':reply_form , 'is_unlike':is_unlike  , 'images':images , 'cart_form':cart_form})


def product_like(request , id) :
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product , id=id)
    if product.like.filter(id = request.user.id).exists():
        product.like.remove(request.user)
    else :
        product.like.add(request.user)
    return redirect(url)

def product_unlike(request , id) :
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product , id=id)
    if product.unlike.filter(id = request.user.id).exists():
        product.unlike.remove(request.user)
    else :
        product.unlike.add(request.user)
    return redirect(url)

def product_comment(request , id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid()  :
            data = comment_form.cleaned_data
            Comment.objects.create(comment = data['comment'] , rate = data['rate'] , user_id = request.user.id ,
                                   product_id=id)
            return redirect(url)
        else:
            return redirect(url)




def product_reply(request , id , cooment_id) :
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' :
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid() :
            data = reply_form.cleaned_data
            Comment.objects.create(comment = data['comment'] , product_id=id , user_id = request.user.id , reply_id = comment_id , is_reply = True)
            return redirect(url)
        else :
            return redirect(url)


def product_search(request):
    products = Product.objects.all()
    if request.method == 'POST' :
        form = searchForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data['search']
            if data.isdigit() :
                products = products.filter(Q(discount__exact = data) | Q(unit_price__exact =data))
            else :
                products = products.filter(Q(name__icontains = data))
            return render(request , 'home/product.html' , {"products" : products})










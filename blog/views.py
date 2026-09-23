from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, Category

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def posts_list(request):
    context = {"posts": Post.objects.filter(is_published=True)}
    return render(request, "posts.html", context)

# def posts_list(request):
#     html = "<h1>Posts List</h1> <p>Bu sehifede butun postlar gosterilecek</p>"
#     for post in POSTS:
#         html += f"<a href='/posts/{post['id']}'>{post['title']}</a></p>"
#     return HttpResponse(html)

def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post tapilmadi")

    # Baxış sayğacı: hər açılışda +1 və bazaya save
    post.views += 1
    post.save()

    context = {"post": post}
    return render(request, "post_detail.html", context)

# def post_detail(request, post_id):
#     html = "<h1>Posts Detail sehifesiu</h1>"
#     for post in POSTS:
#         if post["id"] == post_id:
#             html = f"<h1>{post['title']}</h1>"
#             html += f"<p>Author: {post['author']}</p>"
#             html += f"<p>Category: {post['category']}</p>"
#             html += f"<p>Created at: {post['created_at']}</p>"
#             html += f"<p>{post['content']}</p>"
#             return HttpResponse(html)
#     raise Http404("Post tapilmadi")


def category_list(request):
    context = {"categories": Category.objects.all()}
    return render(request, "category_list.html", context)


def category_detail(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        raise Http404("Category tapilmadi")

    posts = Post.objects.filter(category=category, is_published=True)
    context = {"category": category, "posts": posts}
    return render(request, "category_detail.html", context)


def contact(request):
    return render(request, "contact.html")


def author_posts(request, author_name):
    posts = Post.objects.filter(author=author_name, is_published=True)
    context = {"posts": posts, "author": author_name}
    return render(request, "author_posts.html", context)


def latest(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")[:3]
    context = {"posts": posts}
    return render(request, "latest.html", context)


def stats(request):
    posts = Post.objects.filter(is_published=True)
    top_post = posts.order_by("-views").first()
    context = {
        "post_count": posts.count(),
        "category_count": Category.objects.count(),
        "top_post": top_post,
    }
    return render(request, "stats.html", context)
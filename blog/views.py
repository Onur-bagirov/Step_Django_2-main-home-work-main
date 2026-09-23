from django.shortcuts import render
from django.http import HttpResponse, Http404
from .data import POSTS, CATEGORIES

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def posts_list(request):
    context = {"posts": POSTS}
    return render(request, "posts.html", context)

# def posts_list(request):
#     html = "<h1>Posts List</h1> <p>Bu sehifede butun postlar gosterilecek</p>"
#     for post in POSTS:
#         html += f"<a href='/posts/{post['id']}'>{post['title']}</a></p>"
#     return HttpResponse(html)

def post_detail(request, post_id):
    for post in POSTS:
        if post["id"] == post_id:
            context = {"post": post}
            return render(request, "post_detail.html", context)
    raise Http404("Post tapilmadi")

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
    context = {"categories": CATEGORIES}
    return render(request, "category_list.html", context)


def category_detail(request, category_slug):
    for category in CATEGORIES:
        if category["slug"] == category_slug:
            posts = [post for post in POSTS if post["category"] == category_slug]
            context = {"category": category, "posts": posts}
            return render(request, "category_detail.html", context)
    raise Http404("Category tapilmadi")


def contact(request):
    return render(request, "contact.html")


def author_posts(request, author_name):
    posts = [post for post in POSTS if post["author"] == author_name]
    context = {"posts": posts, "author": author_name}
    return render(request, "author_posts.html", context)


def latest(request):
    posts = POSTS[-3:]
    context = {"posts": posts}
    return render(request, "latest.html", context)


def stats(request):
    context = {"posts": POSTS, "categories": CATEGORIES}
    return render(request, "stats.html", context)
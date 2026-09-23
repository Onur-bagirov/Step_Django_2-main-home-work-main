from datetime import date

from django.db import migrations

CATEGORIES = [
    {"slug": "proqramlasdirma", "name": "Proqramlaşdırma", "description": "Kod, dillər və alətlər"},
    {"slug": "oyunlar", "name": "Oyunlar", "description": "Oyunlar, taktikalar və maraqlı faktlar"},
    {"slug": "kitablar", "name": "Kitablar", "description": "Oxuduqlarımız və tövsiyələr"},
]

POSTS = [
    {
        "title": "Python-da ilk addım", "author": "nigar", "category": "proqramlasdirma",
        "created_at": date(2026, 9, 1),
        "content": "Python öyrənməyə haradan başlamaq lazımdır? Əvvəlcə dəyişənlər, "
                   "sonra şərtlər və döngülər. Ən vacibi isə hər gün bir az kod yazmaqdır.",
        "views": 12, "is_featured": False,
    },
    {
        "title": "Minecraft-da redstone ilə kalkulyator", "author": "murad", "category": "oyunlar",
        "created_at": date(2026, 9, 5),
        "content": "Redstone əslində elektrik dövrəsidir. AND, OR və NOT qapılarından "
                   "istifadə edib oyunun içində işləyən kalkulyator qurmaq olur.",
        "views": 40, "is_featured": True,
    },
    {
        "title": "Git nədir və niyə lazımdır?", "author": "nigar", "category": "proqramlasdirma",
        "created_at": date(2026, 9, 9),
        "content": "Git kodun tarixçəsini saxlayır. Səhv etsən, köhnə versiyaya qayıda "
                   "bilərsən. GitHub isə bu tarixçəni internetdə saxlayan saytdır.",
        "views": 5, "is_featured": False,
    },
    {
        "title": "Harri Potter kitablarını hansı ardıcıllıqla oxumalı?", "author": "aysel", "category": "kitablar",
        "created_at": date(2026, 9, 12),
        "content": "Yeddi kitabın hamısını çıxış ilinə görə oxumaq ən yaxşısıdır. "
                   "Filmlərə isə kitabları bitirəndən sonra baxmağı məsləhət görürəm.",
        "views": 8, "is_featured": False,
    },
    {
        "title": "FIFA-da ən yaxşı taktika", "author": "murad", "category": "oyunlar",
        "created_at": date(2026, 9, 15),
        "content": "4-3-3 sxemi hücum üçün, 5-3-2 isə müdafiə üçün yaxşıdır. "
                   "Amma ən vacibi oyunçuların formasıdır.",
        "views": 15, "is_featured": False,
    },
]


def seed_data(apps, schema_editor):
    Category = apps.get_model("blog", "Category")
    Post = apps.get_model("blog", "Post")

    categories = {}
    for cat in CATEGORIES:
        obj, _ = Category.objects.get_or_create(
            slug=cat["slug"], defaults={"name": cat["name"], "description": cat["description"]}
        )
        categories[cat["slug"]] = obj

    for post in POSTS:
        Post.objects.get_or_create(
            title=post["title"],
            defaults={
                "author": post["author"],
                "category": categories[post["category"]],
                "created_at": post["created_at"],
                "content": post["content"],
                "views": post["views"],
                "is_published": True,
                "is_featured": post["is_featured"],
            },
        )


def remove_data(apps, schema_editor):
    apps.get_model("blog", "Post").objects.all().delete()
    apps.get_model("blog", "Category").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_is_featured"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
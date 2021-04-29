from django import template
from ..models import Category, Article
from datetime import datetime, timedelta
from django.db.models import Count, Q



register = template.Library()

@register.inclusion_tag("shared/navigation.html")
def category_navbar():
    return {
        "categories": Category.objects.get_active_category()
    }

@register.inclusion_tag("shared/popular_articles.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        "popular_articles": Article.objects.get_published_article().annotate(count=Count('hits', filter=Q(articlehit__created__gte=last_month))).order_by('-count', '-publish')[:5]
    }



@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": "account:{}".format(link_name),
        "content": content,
        "classes": classes,
    }

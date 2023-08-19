from newsapp.models import News


def latest_news(request):
    latest_news = News.objects.all().order_by('-publish_time')[:10]
    categories = News.objects.all()

    context = {
        'latest_news': latest_news,
        'categories': categories,
    }

    return context

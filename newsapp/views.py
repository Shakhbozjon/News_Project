
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .forms import ContactForm

from .models import News, Category
def news_list(request):
    # news_list = News.published.all()
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        "news_list": news_list

    }



    return render(request, "news/news_list.html", context)



def news_detail(request, news):
    news = get_object_or_404(News, slug=news)
    context = {
        'news': news
    }

    return render(request, 'news/news_detail.html', context)




# class HomePageView(ListView):
#     model = News
#     template_name = 'news/index.html'



# def ContactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur!")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur!</h2>")

        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)




# def HomePageView(request):
#     categories = Category.objects.all()
#     news_list = News.objects.all().order_by('-publish_time')[:5]
#     local_one =News.objects.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
#     local_news = News.objects.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
#
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'local_one': local_one,
#         'local_news': local_news,
#     }
#
#
#     return render(request, 'news/index.html', context)



class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.all().order_by('-publish_time')[:5]
        context['mahalliy_news'] = News.objects.all().filter(category__name='Mahalliy').order_by('-publish_time')[:5]
        context['sport_news'] = News.objects.all().filter(category__name='Sport').order_by('-publish_time')[:5]
        context['texnologiya_news'] = News.objects.all().filter(category__name='Texnologiya').order_by('-publish_time')[:5]
        context['xorij_news'] = News.objects.all().filter(category__name='Xorij').order_by('-publish_time')[:5]




        return context



class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.objects.filter(category__name='Mahalliy')
        return news



class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.objects.filter(category__name='Sport')
        return news


class XorijNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.objects.filter(category__name='Xorij')
        return news


class TexnologiyaNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologiya_yangiliklar'

    def get_queryset(self):
        news = self.model.objects.filter(category__name='Texnologiya')
        return news




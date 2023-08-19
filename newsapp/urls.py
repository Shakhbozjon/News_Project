from django.urls import path
from .views import (news_list, news_detail, HomePageView, ContactPageView, LocalNewsView,
                    SportNewsView, TexnologiyaNewsView, XorijNewsView, NewsDeleteView,
                    NewsUpdateView, NewsCreateView, admin_page_view, SearchResultsList)

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('mahalliy-yangiliklar/', LocalNewsView.as_view(), name='mahalliy_news_page'),
    path('sport-yangiliklari/', SportNewsView.as_view(), name='sport_news_page'),
    path('texnologiya-yangliklari/', TexnologiyaNewsView.as_view(), name='texno_news_page'),
    path('xorij-yangiliklari/', XorijNewsView.as_view(), name='xorij_news_page'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('admin_page/', admin_page_view, name='admin_page'),
    path('search_result/', SearchResultsList.as_view(), name='search_result'),

]
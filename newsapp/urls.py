from django.urls import path
from .views import news_list, news_detail, HomePageView, ContactPageView, LocalNewsView, SportNewsView, TexnologiyaNewsView, XorijNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('mahalliy-yangiliklar/', LocalNewsView.as_view(), name='mahalliy_news_page'),
    path('sport-yangiliklari/', SportNewsView.as_view(), name='sport_news_page'),
    path('texnologiya-yangliklari/', TexnologiyaNewsView.as_view(), name='texno_news_page'),
    path('xorij-yangiliklari/', XorijNewsView.as_view(), name='xorij_news_page'),
    path('<slug:news>/', news_detail, name='news_detail_page'),

]
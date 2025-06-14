from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('single/', views.single, name='single'),
    path('blog-category-01/', views.blog_category_01, name='blog_category_01'),
    path('blog-category-02/', views.blog_category_02, name='blog_category_02'),
    path('blog-category-03/', views.blog_category_03, name='blog_category_03'),
    path('blog-category-04/', views.blog_category_04, name='blog_category_04'),
    path('blog-category-05/', views.blog_category_05, name='blog_category_05'),
    path('blog-category-06/', views.blog_category_06, name='blog_category_06'),
    path('blog-author/', views.blog_author, name='blog_author'),
    path('contact/', views.contact, name='contact'),
    path('page/', views.default_page, name='default_page'),
    path('page-fullwidth/', views.fullwidth_page, name='fullwidth_page'),
    path('page-404/', views.page_404, name='page_404'),
    path('page-sitemap/', views.sitemap_page, name='sitemap_page'),   
    path('page-skeleton/', views.page_skeleton, name='page_skeleton'),
    path('single-audio/', views.single_audio, name='single_audio'),
    path('single-fullwidth/', views.single_fullwidth, name='single_fullwidth'),
    path('single-no-media/', views.single_no_media, name='single_no_media'),
    path('single-slider/', views.single_slider, name='single_slider'),
    path('single-video/', views.single_video, name='single_video'),
]
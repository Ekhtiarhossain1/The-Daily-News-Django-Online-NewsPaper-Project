from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def single(request):
    return render(request, 'single.html')

def blog_category_01(request):
    return render(request, 'blog-category-01.html')

def blog_category_02(request):
    return render(request, 'blog-category-02.html')

def blog_category_03(request):
    return render(request, 'blog-category-03.html')

def blog_category_04(request):
    return render(request, 'blog-category-04.html')

def blog_category_05(request):
    return render(request, 'blog-category-05.html')

def blog_category_06(request):
    return render(request, 'blog-category-06.html')

def blog_author(request):
    return render(request, 'blog-author.html')

def contact(request):
    return render(request, 'page-contact.html')

def default_page(request):
    return render(request, 'page.html')

def fullwidth_page(request):
    return render(request, 'page-fullwidth.html')

def page_404(request):
    return render(request, 'page-404.html')

def sitemap_page(request):
    return render(request, 'page-sitemap.html')

def page_skeleton(request):
    return render(request, 'page-skeleton.html')

def single_audio(request):
    return render(request, 'single-audio.html')

def single_fullwidth(request):
    return render(request, 'single-fullwidth.html')

def single_no_media(request):
    return render(request, 'single-no-media.html')

def single_slider(request):
    return render(request, 'single-slider.html')

def single_video(request):
    return render(request, 'single-video.html')

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Category

def home(request):
    """Home page with featured articles and latest news"""
    featured_articles = Article.objects.filter(status='published', featured=True)[:3]
    latest_articles = Article.objects.filter(status='published')[:8]
    categories = Category.objects.all()[:6]
    
    context = {
        'featured_articles': featured_articles,
        'latest_articles': latest_articles,
        'categories': categories,
    }
    return render(request, 'news/home.html', context)

def article_detail(request, slug):
    """Display individual article"""
    article = get_object_or_404(Article, slug=slug, status='published')
    related_articles = Article.objects.filter(
        category=article.category, 
        status='published'
    ).exclude(id=article.id)[:4]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'news/article_detail.html', context)

def category_detail(request, slug):
    """Display articles in a specific category"""
    category = get_object_or_404(Category, slug=slug)
    articles_list = Article.objects.filter(
        category=category, 
        status='published'
    )
    
    paginator = Paginator(articles_list, 12)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'news/category_detail.html', context)

def search(request):
    """Search articles"""
    query = request.GET.get('q')
    articles = []
    
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            status='published'
        )
    
    context = {
        'query': query,
        'articles': articles,
    }
    return render(request, 'news/search.html', context)

def about(request):
    """About page"""
    return render(request, 'news/about.html')

def contact(request):
    """Contact page"""
    return render(request, 'news/contact.html')
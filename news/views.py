from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import News, Tag
from .forms import NewsForm

def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', 
    {'all_news': news})

def news_detail(request, pk):
    one_news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', 
    {'news_detail': one_news})

def news_new(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_edit.html', {'form': form})

def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_edit.html', {'form': form})

def news_delete(request, pk):
    try:
        news = News.objects.get(id=pk)
        news.delete()
        return redirect('all_news')
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")


def tag_detail_view(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    news_by_tag = tag.news_set.all()
    return render(request, 'news/news_by_tag.html', 
    {'news_by_tag': news_by_tag})

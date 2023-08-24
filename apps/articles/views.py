from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Article


latest_articles_list = Article.objects.order_by('-pub_date')[:5]


def index(request):
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Post not found")

    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})



def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Article.DoesNotExist:  # Используйте более точное исключение
        raise Http404("Post not found")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(article_id,)))


from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import  Http404
from .models import *
from django.views.decorators.http import require_http_methods,require_GET,require_safe

# Create your views here.

@require_http_methods(["GET"])

#######################index.html##########################################
def index(request):
    latest_posts_list = Post.objects.order_by('publish')[:6]
    #output = ', \n'.join([p.slug for p in latest_posts_list])
    context = {
        'latest_posts_list':latest_posts_list,

    }
    return render(request, 'index.html',context)

#######################detail.html##########################################
@require_GET
def detail(request, post_id):
    post=get_object_or_404(Post,pk =post_id)
    context = {
        'post' : post,
    }
    return render(request,'detail.html', context)

#######################archive.html##########################################
@require_safe
def archive_year(request, year):
    year_archive_posts = get_list_or_404(Post,publish__year = year)
    context = {
        'year_archive_posts': year_archive_posts,
    }
    return render(request, 'archive.html', context)

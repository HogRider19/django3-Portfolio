from django.shortcuts import render, get_object_or_404
from .models import Post 


def all_blog(request):

    page_number = int(request.GET.get('page', 1))

    all_posts = Post.objects.order_by('date')
    post_count = len(all_posts)
    count_all_group = round(post_count/3)

    if page_number <= 0:
        page_number = 1
    elif page_number > count_all_group:
        page_number = count_all_group + 1

    posts = all_posts[(page_number - 1)*3 : (page_number - 1)*3 + 3]

    info_page = {
        'page_number':page_number,
        'next': str(int(page_number) + 1),
        'previous':str(int(page_number) - 1),
        'count_posts': post_count
    }
    
    return render(request, 'blog/all_blogs.html', {'posts' : posts, 'info_page' : info_page})


def detail(request, post_id):

    post = get_object_or_404(Post, pk = post_id)

    return render(request, 'blog/detail.html', {'post' : post})
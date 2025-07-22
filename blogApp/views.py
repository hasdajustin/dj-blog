from django.shortcuts import render,get_object_or_404
from .models import BlogPost

# Create your views here.
def home(request):
    query = request.GET.get('q')
    posts = BlogPost.objects.filter(title__icontains=query) if query else BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
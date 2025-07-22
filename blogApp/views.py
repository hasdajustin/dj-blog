from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def test(request):
    query = request.GET.get('q')
    posts = BlogPost.objects.filter(title__icontains=query) if query else BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})
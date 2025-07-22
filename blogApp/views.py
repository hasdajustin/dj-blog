from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    query = request.GET.get('q')
    posts = BlogPost.objects.filter(title__icontains=query) if query else BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

@login_required
def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})
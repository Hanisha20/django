
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostCreateUpdateForm , CommentCreateForm
from django.utils.text import slugify
from django.views.generic import ListView
from django.db.models import Q

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})
    
class PostDetailView(View):
    form_class = CommentCreateForm
    def get(self, request, post_id, post_slug):
        post = get_object_or_404(Post, slug=post_slug , pk = post_id)
        comments = post.pcomments.filter(is_reply=False)
        return render(request, 'home/detail.html', {'post': post, 'comments': comments , 'form': self.form_class})

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request , post_id):
        post = get_object_or_404(Post, pk = post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'Post deleted successfully', 'success')
        else:
            messages.error(request, 'you cant delete this post', 'danger')
        return redirect('homeApp:home')
class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post,pk = kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id: 
            messages.error(request, 'you cant update this post', 'danger')
            return redirect('homeApp:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args , **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'home/update.html', {'form': form})
    def post(self, request, *args , **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST,instance=post)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.save()
            messages.success(request, 'you updated this post', 'success')
            return redirect('homeApp:post_detail', post.id , post.slug)

class PostCreateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request , 'home/create.html' , {'form': form})
    def post(self, request , *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit= False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'you created new post', 'success')
            return redirect('homeApp:post_detail', new_post.id , new_post.slug)

class SearchPostsView(ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        query = self.request.GET.get('q')  
        if query:
            return Post.objects.filter(Q(user__username__icontains=query) | Q(body__icontains=query))
        else:
            return Post.objects.all()   
<<<<<<< HEAD
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone 
from .models import Post, Comment
from .forms import CommentForm 
def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_date')
    context = {
        'posts': posts,
        'greeting': 'Welcome to my blog!'
    }
    return render(request, 'blog/post_list.html', context)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
   
    comments = post.comments.filter(created_date__lte=timezone.now()).order_by('created_date')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
           
            comment.author = request.user.username if request.user.is_authenticated else "Anonymous" 
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
       
        form = CommentForm()

    
    return render(request, 'blog/post_detail.html', {
        'post': post, 
        'comments': comments, 
        'form': form
    })

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
  
    if request.user.is_superuser:
        comment.delete()
    
    return redirect('post_detail', pk=comment.post.pk)



def post_delete(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    
   
    if request.user.is_superuser:
        post.delete()
        
        return redirect('blog_list')
    else:
        
        return redirect('post_detail', pk=post.pk)
>>>>>>> 25d3f77 (Deployment files setup and project initialization)

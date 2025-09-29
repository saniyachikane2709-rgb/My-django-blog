from django.db import models
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


from django.contrib.auth.models import User 

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    is_published = models.BooleanField(default=False) 
    published_date = models.DateTimeField(blank=True, null=True) 

    class Meta:

        ordering = ['-published_date', 'created_at']

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    author = models.CharField(max_length=200)
    text = models.TextField() 
    created_date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.text[:20] + '...' 

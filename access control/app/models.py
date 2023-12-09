from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

class PostImage(models.Model):
    image = models.ImageField(upload_to='post_images', max_length=1000)
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)

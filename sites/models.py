from django.contrib.auth.models import User
from django.db import models

class Site(models.Model):
    title = models.CharField(max_length=250)
    site = models.CharField(max_length=250)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='likes_dislikes')
    is_like = models.BooleanField()  # True -> Like, False -> Dislike

    class Meta:
        unique_together = ('user', 'site')



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user} {self.site} {self.body}"

class CommentLikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes_dislikes')
    is_like = models.BooleanField()  # True -> Like, False -> Dislike

    class Meta:
        unique_together = ('user', 'comment')

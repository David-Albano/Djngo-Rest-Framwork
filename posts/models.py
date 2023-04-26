from django.db import models as md

class Post(md.Model):
    created = md.DateTimeField(auto_now_add=True)
    title = md.CharField(max_length=100, blank=False)
    content = md.TextField()
    author = md.CharField(max_length=100, blank=False)
    owner = md.ForeignKey('auth.user', related_name='posts', on_delete=md.CASCADE)

    class Meta:
        ordering = ['created']

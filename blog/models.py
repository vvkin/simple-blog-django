from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20, default='')
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def short_text(self):
        if len(self.body) > 500:
            return self.body[:500] + '...'
        else:
            return self.body

    def full_text(self):
        return self.body

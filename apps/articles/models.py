import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField('Article Title', max_length=255, null=False)
    content = models.TextField('Article Content',  null=False)
    pub_date = models.DateTimeField('Article Publish Date', null=False)

    def __str__(self):
        return self.title

    def was_publish_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Comment author name', max_length=80, null=False)
    comment_text = models.CharField('Comment text', max_length=255, null=False)

    def __str__(self):
        return self.author_name
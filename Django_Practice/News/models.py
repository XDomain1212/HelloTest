from django.db import models

# Create your models here.

class News(models.Model):
    News_title=models.CharField(max_length=200)
    News_context=models.CharField(max_length=2000)
    News_pub_date=models.DateField('news published date')

class News_Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    news_comment_text=models.CharField(max_length=2000)
    news_comment_pub_date=models.DateField('comment published date')

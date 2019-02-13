from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)  # 自动使用发布文章时的时间
    content = models.TextField()

    def __str__(self):
        return self.title

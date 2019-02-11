from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200, null=False, unique=True)
    pub_date = models.DateField()

    def __str__(self):
        return '<问题：%s>' % self.question

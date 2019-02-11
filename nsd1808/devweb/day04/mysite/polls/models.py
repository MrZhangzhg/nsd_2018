from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200, null=False, unique=True)
    pub_date = models.DateField()

    def __str__(self):
        return '<问题：%s>' % self.question

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # q = models.ForeignKey(Question, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "<%s=>%s>" % (Question, self.choice_text)


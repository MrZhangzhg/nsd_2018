from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True, null=False)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField()
    q = models.ForeignKey(Question)

    def __str__(self):
        return "%s=>%s: %s" % (self.q, self.choice_text, self.votes)

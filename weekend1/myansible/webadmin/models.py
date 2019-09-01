from django.db import models

# Create your models here.

class Group(models.Model):
    groupname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(Group)

    def __str__(self):
        return "%s: %s=>%s" % (self.group, self.hostname, self.ipaddr)

class Module(models.Model):
    modulename = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.modulename

class Arg(models.Model):
    arg_text = models.CharField(max_length=100)
    module = models.ForeignKey(Module)

    def __str__(self):
        return "%s: %s" % (self.module, self.arg_text)

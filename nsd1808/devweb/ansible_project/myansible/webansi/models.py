from django.db import models

class HostGroup(models.Model):
    group_name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.group_name

class Host(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)

    def __str__(self):
        return "%s => %s" % (self.hostname, self.group)

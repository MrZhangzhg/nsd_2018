from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=100, unique=True, null=False)
    ipaddr = models.CharField(max_length=15, null=False)
    group = models.ForeignKey(HostGroup)

    def __str__(self):
        return '%s => %s' % (self.hostname, self.group)

class Module(models.Model):
    module_name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.module_name

class Argument(models.Model):
    argument_text = models.CharField(max_length=100, unique=True, null=False)
    module = models.ForeignKey(Module)

    def __str__(self):
        return "%s => %s" % (self.module, self.argument_text)

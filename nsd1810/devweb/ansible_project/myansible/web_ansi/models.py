from django.db import models

class HostGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.group_name

class Host(models.Model):
    hostname = models.CharField(max_length=100, unique=True)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)

    def __str__(self):
        return '%s:%s=> %s' % (self.hostname, self.ipaddr, self.group)

class Module(models.Model):
    module_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.module_name

class Argument(models.Model):
    args_text = models.CharField(max_length=200, unique=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return "%s=> %s" % (self.module, self.args_text)

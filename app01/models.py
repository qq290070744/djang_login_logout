# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userpro(models.Model):
    user=models.OneToOneField(User)
    name=models.CharField(u'姓名',max_length=30)
    def __unicode__(self):
        return self.name

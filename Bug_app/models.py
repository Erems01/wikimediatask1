from django.db import models


class Bug_app(models.Models):

     BUG_TYPES = (
        ('error'), 
        ('new feature'), 
        ('code','code'),
        ('enhancement')
    )

     STATUS = (
        ('To do'),
        ('In Progress','In Progress'),
        ('Done','Done')
    ) 

    #field for bug description
description = models.TextField() 

    #field for bug type
bug_type = models.CharField(max_length=100)

    #field for report date
report_date = models.Datefield()
    #field for status
status = models.CharField(max_lenght=50)

def __str__(self):
        return self.description

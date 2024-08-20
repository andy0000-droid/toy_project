from django.db import models


# Create your models here.
class Posting(models.Model):
    # id # hex or int
    id = models.IntegerField()
    # tttle # text
    title = models.TextField()
    # abstract # test
    abstrack = models.TextField()
    # time # date
    time = models.DateTimeField(auto_now=False)
    # content # bin
    content = models.TextField()
    # cat # text
    cat = models.TextField()
    # like # text
    like = models.IntegerField()
    # posted # bool
    posted = models = BooleaField(initial=False)
    
    def __str__(self):
        
        return self.title
    


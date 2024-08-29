from django.db import models


# Create your models here.
class Profile(models.Model):
    addr = models.TextField()
    name = models.TextField()
    about = models.TextField()
    cat = models.TextField()
    img = models.ImageField()

    def __str__(self):
        _name = name
        _addr = addr
        return _name + "의" + _addr + "블로그 입니다."
    # Create
    

    # Read

    # Update

    # Delete

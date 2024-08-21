from django.db import models


# Create your models here.
class Profile(models.Model):
    # addr # text
    addr = models.TextField()
    # name # text
    name = models.TextField()
    # about # text
    about = models.TextField()
    # cat # text
    cat = models.TextField()
    # img # bin
    img = models.ImageField()
    # Create

    # Read

    # Update

    # Delete

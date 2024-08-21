from django.db import models


# Create your models here.
class Profile(models.Model):
    addr = models.TextField()
    name = models.TextField()
    about = models.TextField()
    cat = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return str(self.name)

    # Create

    # Read

    # Update

    # Delete

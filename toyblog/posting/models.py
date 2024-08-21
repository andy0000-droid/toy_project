"""
Posting Database
"""

from django.db import models
from django.contrib.auth import get_user_model
from writing import models as post_db


def db_error():
    """
    Print error when occured
    """

    print("Database error occured")
    print("Accssing a Database that has not been created")
    return get_user_model().objects.get_or_create(id=-1)


class Posting(models.Model):
    """
    post: Get Foreign Database from writing
    like: The number of likes for Post
    """

    post = models.ForeignKey(post_db, on_delete=models.SET(db_error))
    like = models.IntegerField()
    # Read

    # Update

    # Delete

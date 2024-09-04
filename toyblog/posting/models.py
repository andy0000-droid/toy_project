"""
Posting Database
"""

from django.db import models
from django.contrib.auth import get_user_model
from writing import models as post_db
from log_sender import send_log


def db_error(uid):
    """
    Print error when occured
    """

    print("Database error occured")
    print("Accssing a Database that has not been created")
    send_log("Accessing a Database that has not been created")
    send_log(f"Access from {uid}")
    return get_user_model().objects.get_or_create(id=-1)


class Posting(models.Model):
    """
    post: Get Foreign Database from writing
    like: The number of likes for Post
    """

    post = models.ForeignKey(
        post_db, on_delete=models.SET(db_error), verbose_name="Get Posting Database"
    )
    like = models.IntegerField(verbose_name="The number of like")
    comment = models.TextField(blank=True)
    # Read

    # Update

    # Delete

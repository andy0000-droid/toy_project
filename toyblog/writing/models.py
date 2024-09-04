"""
Writing Database
"""

from django.db import models


class Writing(models.Model):
    """
    Class for Database
    id: Post ID
    title: Post Title
    abstract: Post Abstract
    time: First written time
    update_time: Update time
    content: Post content
    cat: Category of Post
    publish: Post is published or not
    """

    id = models.IntegerField(verbose_name="Post ID")
    title = models.TextField(blank=False, verbose_name="Post Title")
    abstract = models.TextField(verbose_name="Post Abstract")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Writing Time")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Post Update Time")
    content = models.TextField(blank=False, verbose_name="Post Content")
    cat = models.TextField(verbose_name="Post Category")
    publish = models.BooleanField(
        default=False, verbose_name="Checking for Publish or Temporally Saved"
    )

    def __str__(self):
        res_str = "ID: " + self.id + "\nTitle: " + self.title
        return res_str

    # Create

    # Read

    # Update

    # Delete

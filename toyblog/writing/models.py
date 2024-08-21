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

    id = models.IntegerField()
    title = models.TextField()
    abstract = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    cat = models.TextField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        res_str = "ID: " + self.id + "\nTitle: " + self.title
        return res_str

    # Create

    # Read

    # Update

    # Delete

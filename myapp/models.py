from django.db import models



class Suggestion:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class User(models.Model):
    def __init__(self, email):
        self.email = email
        
    def get_sug(self, title, content):
        sug = Suggestion(title, content)
        # return Suggestion object
        return sug

class Board(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return '%s' % self.title

class Account(models.Model):
    """
    Table Schema to store articles.
    """
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=16)

    def __str__(self):
        return '%s' % self.email
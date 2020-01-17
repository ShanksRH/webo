from django.db import models
import json

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    ava = models.CharField(max_length=250)
    ref = models.CharField(max_length=30, unique=True)
    article_id = models.IntegerField()

    def __str__(self):
        js = {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'ava' : self.ava,
            'ref' : self.ref,
            'article_id' : self.article_id
        }
        return json.dumps(js)
    
    def toDict(self):
        js = {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'ava' : self.ava,
            'ref' : self.ref,
            'article_id' : self.article_id
        }
        return js

class UserGame(models.Model):
    user_id = models.IntegerField(primary_key=True)
    games_ids = models.CharField(max_length=250)

from django.db import models
import json

class Achieve(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    text = models.TextField()
    def __str__(self):
        js = {
            'id' : self.id,
            'name' : self.name,
            'text' : self.text
        }
        return json.dumps(js)

class UserAchieve(models.Model):
    user_id = models.IntegerField(primary_key=True)
    articles_ids = models.CharField(max_length=250)

    def __str__(self):
        js = {
            'user_id' : self.user_id,
            'articles_ids' : self.articles_ids
        }
        return json.dumps(js)

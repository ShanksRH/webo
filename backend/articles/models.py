from django.db import models
import json

class Article(models.Model):
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
    
    def toDict(self):
        js = {
            'id' : self.id,
            'name' : self.name,
            'text' : self.text
        }
        return js
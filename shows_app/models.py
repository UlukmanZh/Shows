from django.db import models

class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10 and len(postData['desc']) != 0:
            errors["desc"] = "Show description should be at least 10 characters"
        if len(postData['date']) < 1:
            errors["date"] = "Date should not be empty"
        
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name



class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='post')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title




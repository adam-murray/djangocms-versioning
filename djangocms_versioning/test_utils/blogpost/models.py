from django.db import models


class BlogPost(models.Model):
    name = models.TextField()

    def __str__(self):
        return "{} ({})".format(self.name, self.pk)


class BlogContent(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    language = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.text


class Comment(models.Model):
    # NOTE: The BlogPost model is technically the grouper for comments
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
from django.db import models
from datetime import datetime

from django.urls import reverse

class Post(models.Model):
    title = models.CharField("Day", max_length=100)
    main_image = models.ImageField("Main image", upload_to="main_ars_images/")
    quote = models.TextField("Favorite quote", default="")
    text = models.TextField("What happened today?", default="")
    published = models.DateTimeField("Date", default=datetime.now())
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.id})

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Days"

class ArticleImages(models.Model):
    title = models.CharField("Title", max_length=100)
    image = models.ImageField("Image", upload_to="article_images/")
    post = models.ForeignKey(Post, verbose_name="Day", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Image for a day"
        verbose_name_plural = "Images for a days"
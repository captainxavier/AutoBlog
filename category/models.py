from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


    def __str__(self):
        return self.title


  



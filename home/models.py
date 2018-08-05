from __future__ import unicode_literals

from django.db import models


#blog
class Article_Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    class Meta:
        db_table = "articles_categories"
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 50)
    url_title = models.CharField(max_length = 100 , null = True)
    text = models.CharField(max_length = 500000)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to = 'home/static/images/articles_images', null = True)
    category = models.ForeignKey(Article_Category, on_delete=models.CASCADE)
    class Meta:
        db_table = "articles"

#case studies
class CaseStudy_Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    class Meta:
        db_table = "case_studies_categories"
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 200)
    class Meta:
        db_table = "clients"
    def __str__(self):
        return self.name

class CaseStudy(models.Model):
    title = models.CharField(max_length = 50)
    url_title = models.CharField(max_length = 100 , null = True)
    description = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000 , null = True)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to = 'home/static/images/case_studies_images', null = True)
    category = models.ForeignKey(CaseStudy_Category, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    class Meta:
        db_table = "case_studies"

#users
class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    e_mail = models.CharField(max_length = 50)
    image = models.ImageField(null = True)
    class Meta:
        db_table = "users"
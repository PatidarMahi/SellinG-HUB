from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    
    @staticmethod
    def get_category_id_by_name(category_name):
        category=Category.objects.get(name=category_name)
        return category.id 

 

    def __str__(self):
        return  self.name



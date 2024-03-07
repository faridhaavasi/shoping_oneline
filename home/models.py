from django.db import models
from django.template.defaultfilters import slugify
from .managers import ProductManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}-{self.created_at}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Category, self).save()


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/images/%Y/%m/%d')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return f'{self.name}-{self.created}-{self.available}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Product, self).save()







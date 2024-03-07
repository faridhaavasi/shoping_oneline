from django.db import models


class ProductManager(models.Manager):
    def available_True_manager(self):
        return self.filter(available=True)



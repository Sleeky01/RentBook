from django.db import models

# Create your models here.
from django.db import models

class Rentbook(models.Model):
    book_title = models.CharField(max_length=255)
    renter_name = models.CharField(max_length=255)
    rent_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book_title} - {self.renter_name}"

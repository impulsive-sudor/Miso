from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('check', 'Check'),
    ('credit', 'Credit'),
]

class GeneralModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE, null=True, blank=True, related_name='created_%(class)s')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_%(class)s')

    class Meta:
        abstract = True

class PropertyCategory(GeneralModel):
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Property(GeneralModel):
    name = models.CharField(max_length=100)
    TYPE_OF_PROPERTY = [
        ('single family residence', 'Single Family Residence'),
        ('multi-family residence', 'Multi-Family Residence'),
        ('vacation or short term rental', 'Vacation/Short-Term Rental'),
        ('commercial property', 'Commercial Property'),
        ('land', 'Land'),
        ('royalties', 'Royalties'),
        ('self-rental', 'Self-Rental'),
        ('other', 'Other'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_OF_PROPERTY, default='single family residence')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Contact(GeneralModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class PropertyExpense(GeneralModel):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(null=True, blank=True)
    category = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True, choices=PAYMENT_METHOD_CHOICES)
    receipts = models.FileField(upload_to='receipts/', null=True, blank=True)

    def __str__(self):
        return self.name

class Vehicle(GeneralModel):
    name = models.CharField(max_length=100)
    business_use = models.BooleanField(default=False)
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    make = models.CharField(max_length=100, null=True, blank=True)
    vin = models.CharField(max_length=100, null=True, blank=True)
    license_plate = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Mile(GeneralModel):
    name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=255)
    date = models.DateField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    source_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Income(GeneralModel):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True, choices=PAYMENT_METHOD_CHOICES)
    receipts = models.FileField(upload_to='receipts/', null=True, blank=True)

    def __str__(self):
        return self.name

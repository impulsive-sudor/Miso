# myapp/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from accounter.models import PropertyCategory

# Create default categories according to what's required for taxes
# Reference https://www.irs.gov/pub/irs-pdf/f1040se.pdf
@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    PropertyCategory.objects.get_or_create(name='Advertising', defaults={'notes': 'Costs incurred to advertise the rental property to potential tenants.'})
    PropertyCategory.objects.get_or_create(name='Auto and travel', defaults={'notes': 'Expenses related to travel for the purposes of managing the rental property.'})
    PropertyCategory.objects.get_or_create(name='Cleaning and Maintenance', defaults={'notes': 'Costs for cleaning services and maintenance of the property.'})
    PropertyCategory.objects.get_or_create(name='Commissions', defaults={'notes': 'Commissions paid to property managers or real estate agents.'})
    PropertyCategory.objects.get_or_create(name='Insurance', defaults={'notes': 'Insurance premiums for the rental property.'})
    PropertyCategory.objects.get_or_create(name='Legal and Professional Services', defaults={'notes': 'Costs for legal and professional services such as attorney or accountant fees.'})
    PropertyCategory.objects.get_or_create(name='Management Fees', defaults={'notes': 'Costs for property management services.'})
    PropertyCategory.objects.get_or_create(name='Mortgage Interest Paid to Banks', defaults={'notes': 'Interest paid on loans used to acquire or improve rental property.'})
    PropertyCategory.objects.get_or_create(name='Other Interest', defaults={'notes': 'Interest paid on other loans related to the rental property.'})
    PropertyCategory.objects.get_or_create(name='Repairs', defaults={'notes': 'Costs for repairs and maintenance of the property.'})
    PropertyCategory.objects.get_or_create(name='Supplies', defaults={'notes': 'Costs for supplies used in the rental property.'})
    PropertyCategory.objects.get_or_create(name='Taxes', defaults={'notes': 'Property taxes paid on the rental property.'})
    PropertyCategory.objects.get_or_create(name='Utilities', defaults={'notes': 'Costs for utilities such as electricity, gas, water, and sewer.'})
    PropertyCategory.objects.get_or_create(name='Depreciation expense or depletion', defaults={'notes': 'Depreciation of the rental property.'})
    PropertyCategory.objects.get_or_create(name='Other', defaults={'notes': 'Other expenses related to the rental property.'})
# myapp/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from accounter.models import PropertyCategory, BusinessCategory

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
    # Reference https://www.irs.gov/pub/irs-pdf/f1040sc.pdf
    BusinessCategory.objects.get_or_create(name='Advertising', defaults={'notes': 'Costs incurred to advertise the business.'})
    BusinessCategory.objects.get_or_create(name='Car and Truck Expenses', defaults={'notes': 'Costs for the business use of vehicles.'})
    BusinessCategory.objects.get_or_create(name='Commissions and Fees', defaults={'notes': 'Commissions and fees paid for the business.'})
    BusinessCategory.objects.get_or_create(name='Contract Labor', defaults={'notes': 'Costs for contract labor.'})
    BusinessCategory.objects.get_or_create(name='Depletion', defaults={'notes': 'Depletion of natural resources.'})
    BusinessCategory.objects.get_or_create(name='Depreciation', defaults={'notes': 'Depreciation of business assets.'})
    BusinessCategory.objects.get_or_create(name='Employee Benefits Programs', defaults={'notes': 'Costs for employee benefit programs.'})
    BusinessCategory.objects.get_or_create(name='Insurance', defaults={'notes': 'Insurance premiums for the business.'})
    BusinessCategory.objects.get_or_create(name='Interest', defaults={'notes': 'Interest paid for the business.'})
    BusinessCategory.objects.get_or_create(name='Legal and Professional Services', defaults={'notes': 'Costs for legal and professional services such as attorney or accountant fees.'})
    BusinessCategory.objects.get_or_create(name='Office Expenses', defaults={'notes': 'Costs for office supplies and expenses.'})
    BusinessCategory.objects.get_or_create(name='Pension and Profit-Sharing Plans', defaults={'notes': 'Costs for pension and profit-sharing plans.'})
    BusinessCategory.objects.get_or_create(name='Rent or Lease', defaults={'notes': 'Costs for renting or leasing business property.'})
    BusinessCategory.objects.get_or_create(name='Repairs and Maintenance', defaults={'notes': 'Costs for repairs and maintenance of business property.'})
    BusinessCategory.objects.get_or_create(name='Supplies', defaults={'notes': 'Costs for supplies used in the business.'})
    BusinessCategory.objects.get_or_create(name='Taxes and Licenses', defaults={'notes': 'Taxes and licenses paid for the business.'})
    BusinessCategory.objects.get_or_create(name='Travel', defaults={'notes': 'Costs for business travel.'})
    BusinessCategory.objects.get_or_create(name='Meals and Entertainment', defaults={'notes': 'Costs for business meals and entertainment.'})
    BusinessCategory.objects.get_or_create(name='Utilities', defaults={'notes': 'Costs for utilities such as electricity, gas, water, and sewer.'})
    BusinessCategory.objects.get_or_create(name='Wages', defaults={'notes': 'Wages paid to employees.'})
    BusinessCategory.objects.get_or_create(name='Other', defaults={'notes': 'Other expenses related to the business.'})

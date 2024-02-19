import pytest
import datetime

from .utils import get_sub_orgs
from evercycle_models.models.organization import Organization
from evercycle_models.models.address import Address
from evercycle_models.models.contact import Contact


@pytest.mark.django_db
def test_get_org():
    test_address = Address.objects.create(
        id=1,
        address1='25 person st',
        address2='',
        country='US',
        postal_code='123121',
        created_at=datetime.datetime.now(),
        created_by=0,
        updated_at=datetime.datetime.now(),
        updated_by=0,
        location_name='',
        state='IL',
        city='Chicago',
    )

    test_contact = Contact.objects.create(
        id=1,
        created_at=datetime.datetime.now(),
        first_name='Joe',
        last_name='Moe',
        email='joe@evercycle.io',
        updated_by=0,
        updated_at=datetime.datetime.now()
    )

    test_org = Organization.objects.create(
        id=212,
        name="Test Organization",
        organization_type='test',
        address=test_address,
        tax_id=0,
        updated_by=0,
        updated_at=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        logo='',
        main_contact=test_contact
    )

    org = Organization.objects.get(id=test_org.id)
    organization = get_sub_orgs(organization=org)

    assert filter(lambda x: x.id == 212, organization)

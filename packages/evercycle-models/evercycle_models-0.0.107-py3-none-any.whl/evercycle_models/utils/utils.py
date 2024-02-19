from typing import List, Union, Any, Callable

from evercycle_models.models import Organization


def get_sub_orgs(
    organization: Organization,
    organizations_list: List[Union[Organization, Any]] = None,
    map_data_for_list: Callable[[Organization], List[Union[Organization, Any]]] = None
):
    if organizations_list is None:
        organizations_list = []

    if map_data_for_list is not None:
        organizations_list.extend(map_data_for_list(organization))
    else:
        organizations_list.append(organization)

    sub_organizations = organization.sub_organizations.all()

    for sub_organization in sub_organizations:
        get_sub_orgs(
            organization=sub_organization,
            organizations_list=organizations_list,
            map_data_for_list=map_data_for_list
        )

    return organizations_list

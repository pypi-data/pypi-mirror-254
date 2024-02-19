from django.contrib import admin
from evercycle_models.models.address import Address
from evercycle_models.models.carrier import Carrier
from evercycle_models.models.carrier_type import CarrierType
from evercycle_models.models.certification import Certification
from evercycle_models.models.contact import Contact
from evercycle_models.models.organization import Organization
from evercycle_models.models.processor import Processor
from evercycle_models.models.service_level import ServiceLevel
from evercycle_models.models.service_provider import ServiceProvider
from evercycle_models.models.service_provider_service import ServiceProviderService
from evercycle_models.models.workflow import Workflow
from evercycle_models.models.workflow_type import WorkflowType

admin.site.register(Address)
admin.site.register(Carrier)
admin.site.register(CarrierType)
admin.site.register(Certification)
admin.site.register(Contact)
admin.site.register(Organization)
admin.site.register(Processor)
admin.site.register(ServiceLevel)
admin.site.register(ServiceProvider)
admin.site.register(ServiceProviderService)
admin.site.register(Workflow)
admin.site.register(WorkflowType)

"""
from evercycle_models.models.asset import Asset
from evercycle_models.models.asset_damage_type import AssetDamageType
from evercycle_models.models.asset_history import AssetHistory
from evercycle_models.models.asset_status import AssetStatus
from evercycle_models.models.asset_type import AssetType
from evercycle_models.models.audit import Audit
from evercycle_models.models.box_notification import BoxNotification
from evercycle_models.models.box_status import BoxStatus
from evercycle_models.models.carrier import Carrier
from evercycle_models.models.column_visibility import ColumnVisibility
from evercycle_models.models.country_codes import CountryCodes
from evercycle_models.models.data_erasure import DataErasure
from evercycle_models.models.delivered import Delivered
from evercycle_models.models.device_list_type import DeviceListType
from evercycle_models.models.device_master_list import DeviceMasterList
from evercycle_models.models.device_master_list_hold import DeviceMasterListHold
from evercycle_models.models.device_type import DeviceType
from evercycle_models.models.dispatched import Dispatched
from evercycle_models.models.dmd_devices import DmdDevices
from evercycle_models.models.dmd_receive_status import DmdReceiveStatus
from evercycle_models.models.dmd_receiving_journal import DmdReceivingJournal
from evercycle_models.models.dmd_sf import DmdSf
from evercycle_models.models.flatfile_request import FlatfileRequest
from evercycle_models.models.flatfile_upload import FlatfileUpload
from evercycle_models.models.geolocation_data import GeolocationData
from evercycle_models.models.image import Image
from evercycle_models.models.integration_user import IntegrationUser
from evercycle_models.models.integrations import Integrations
from evercycle_models.models.inventory import Inventory
from evercycle_models.models.invoiced_1 import Invoiced1
from evercycle_models.models.invoiced_2 import Invoiced2
from evercycle_models.models.lookup_recycling_processor import LookupRecyclingProcessor
from evercycle_models.models.organization_collection import OrganizationCollection
from evercycle_models.models.organization_integration import OrganizationIntegration
from evercycle_models.models.organization_integrations import OrganizationIntegrations
from evercycle_models.models.package_type import PackageType
from evercycle_models.models.packages_received import PackagesReceived
from evercycle_models.models.pdf import Pdf
from evercycle_models.models.pricebook import Pricebook
from evercycle_models.models.pricebook_catalog import PricebookCatalog
from evercycle_models.models.pricebook_catalog_price import PricebookCatalogPrice
from evercycle_models.models.processor import Processor
from evercycle_models.models.program import Program
from evercycle_models.models.program_collection import ProgramCollection
from evercycle_models.models.program_device_quantity import ProgramDeviceQuantity
from evercycle_models.models.program_type import ProgramType
from evercycle_models.models.purchaser import Purchaser
from evercycle_models.models.pyxera_form_data import PyxeraFormData
from evercycle_models.models.quote import Quote
from evercycle_models.models.quote_history import QuoteHistory
from evercycle_models.models.replaced_tracking import ReplacedTracking
from evercycle_models.models.request import Request
from evercycle_models.models.request_box_quantity import RequestBoxQuantity
from evercycle_models.models.request_device_quantity import RequestDeviceQuantity
from evercycle_models.models.request_device_type import RequestDeviceType
from evercycle_models.models.request_type import RequestType
from evercycle_models.models.role import Role
from evercycle_models.models.service_provider import ServiceProvider
from evercycle_models.models.service_provider_services import ServiceProviderServices
from evercycle_models.models.session import Session
from evercycle_models.models.settings import Settings
from evercycle_models.models.shipping_status import ShippingStatus
from evercycle_models.models.shipping_status_detail_easypost import ShippingStatusDetailEasypost
from evercycle_models.models.shipping_status_easypost import ShippingStatusEasypost
from evercycle_models.models.sp_pricebook import SpPricebook
from evercycle_models.models.test import Test
from evercycle_models.models.test_attributes import TestAttributes
from evercycle_models.models.tracked_box import TrackedBox
from evercycle_models.models.tracked_box_csv import TrackedBoxCsv
from evercycle_models.models.tracking import Tracking
from evercycle_models.models.tracking_status import TrackingStatus
from evercycle_models.models.upload import Upload
from evercycle_models.models.wip_device_master_list import WipDeviceMasterList
"""
"""
admin.site.register(Asset)
admin.site.register(AssetDamageType)
admin.site.register(AssetHistory)
admin.site.register(AssetStatus)
admin.site.register(Audit)
admin.site.register(BoxNotification)
admin.site.register(BoxStatus)
admin.site.register(Carrier)
admin.site.register(ColumnVisibility)
admin.site.register(Contact)
admin.site.register(CountryCodes)
admin.site.register(DataErasure)
admin.site.register(Delivered)
admin.site.register(DeviceListType)
admin.site.register(DeviceMasterList)
admin.site.register(DeviceMasterListHold)
admin.site.register(DeviceType)
admin.site.register(Dispatched)
admin.site.register(DmdDevices)
admin.site.register(DmdReceiveStatus)
admin.site.register(DmdReceivingJournal)
admin.site.register(DmdSf)
admin.site.register(FlatfileRequest)
admin.site.register(FlatfileUpload)
admin.site.register(GeolocationData)
admin.site.register(Image)
admin.site.register(IntegrationUser)
admin.site.register(Integrations)
admin.site.register(Inventory)
admin.site.register(Invoiced1)
admin.site.register(Invoiced2)
admin.site.register(LookupRecyclingProcessor)
admin.site.register(OrganizationCollection)
admin.site.register(OrganizationIntegration)
admin.site.register(OrganizationIntegrations)
admin.site.register(PackageType)
admin.site.register(PackagesReceived)
admin.site.register(Pdf)
admin.site.register(Pricebook)
admin.site.register(PricebookCatalog)
admin.site.register(PricebookCatalogPrice)
admin.site.register(Processor)
admin.site.register(Program)
admin.site.register(ProgramCollection)
admin.site.register(ProgramDeviceQuantity)
admin.site.register(ProgramType)
admin.site.register(Purchaser)
admin.site.register(PyxeraFormData)
admin.site.register(Quote)
admin.site.register(QuoteHistory)
admin.site.register(ReplacedTracking)
admin.site.register(Request)
admin.site.register(RequestBoxQuantity)
admin.site.register(RequestDeviceQuantity)
admin.site.register(RequestDeviceType)
admin.site.register(RequestType)
admin.site.register(Role)
admin.site.register(ServiceProvider)
admin.site.register(ServiceProviderServices)
admin.site.register(Session)
admin.site.register(Settings)
admin.site.register(ShippingStatus)
admin.site.register(ShippingStatusEasypost)
admin.site.register(ShippingStatusDetailEasypost)
admin.site.register(SpPricebook)
admin.site.register(Test)
admin.site.register(TestAttributes)
admin.site.register(TrackedBox)
admin.site.register(TrackedBoxCsv)
admin.site.register(Tracking)
admin.site.register(TrackingStatus)
admin.site.register(Upload)
admin.site.register(WipDeviceMasterList)
"""

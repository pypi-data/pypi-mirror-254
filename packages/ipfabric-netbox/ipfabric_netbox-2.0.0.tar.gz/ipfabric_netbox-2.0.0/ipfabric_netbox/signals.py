from typing import Optional

from dcim.models import Device
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from extras.choices import CustomFieldTypeChoices
from extras.choices import CustomLinkButtonClassChoices
from extras.models import CustomField
from extras.models import CustomLink
from packaging import version

from .models import IPFabricBranch
from .models import IPFabricSource

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)

if NETBOX_CURRENT_VERSION >= version.parse("3.7.0"):
    from extras.choices import (
        CustomFieldUIVisibleChoices as CustomFieldUIVisibleChoices,
    )
    from extras.choices import CustomFieldUIEditableChoices
else:
    from extras.choices import (
        CustomFieldVisibilityChoices as CustomFieldUIVisibleChoices,
    )


def create_custom_field(
    field_name: str,
    label: str,
    models: list,
    object_type=None,
    cf_type: Optional[str] = "type_text",
    ui_visibility: Optional[str] = "VISIBILITY_READ_ONLY",
):
    if NETBOX_CURRENT_VERSION >= version.parse("3.7.0"):
        defaults = {
            "label": label,
            "object_type": ContentType.objects.get_for_model(object_type)
            if object_type
            else None,
            "ui_visible": getattr(CustomFieldUIVisibleChoices, "ALWAYS"),
            "ui_editable": getattr(CustomFieldUIEditableChoices, "NO"),
        }
    else:
        defaults = {
            "label": label,
            "object_type": ContentType.objects.get_for_model(object_type)
            if object_type
            else None,
            "ui_visibility": getattr(
                CustomFieldUIVisibleChoices, "VISIBILITY_READ_ONLY"
            ),
        }

    custom_field, _ = CustomField.objects.update_or_create(
        type=getattr(CustomFieldTypeChoices, cf_type.upper()),
        name=field_name,
        defaults=defaults,
    )

    for model in models:
        custom_field.content_types.add(ContentType.objects.get_for_model(model))


def ipfabric_netbox_init():
    create_custom_field(
        "ipfabric_source",
        "IP Fabric Source",
        [Device],
        cf_type="type_object",
        object_type=IPFabricSource,
    )
    create_custom_field(
        "ipfabric_branch",
        "IP Fabric Last Sync",
        [Device],
        cf_type="type_object",
        object_type=IPFabricBranch,
    )
    cl, _ = CustomLink.objects.update_or_create(
        defaults={
            "link_text": "{% if object.custom_field_data.ipfabric_source is defined %}{% set SOURCE_ID = object.custom_field_data.ipfabric_source %}{% if SOURCE_ID %}IP Fabric{% endif %}{% endif %}",
            "link_url": '{% if object.custom_field_data.ipfabric_source is defined %}{% set SOURCE_ID = object.custom_field_data.ipfabric_source %}{% if SOURCE_ID %}{% set BASE_URL = object.custom_fields.filter(object_type__model="ipfabricsource").first().object_type.model_class().objects.get(pk=SOURCE_ID).url %}{{ BASE_URL }}/inventory/devices?options={"filters":{"sn": ["like","{{ object.serial }}"]}}{% endif %}{%endif%}',
            "new_window": True,
            "button_class": CustomLinkButtonClassChoices.BLUE,
        },
        name="ipfabric",
    )
    cl.content_types.add(ContentType.objects.get_for_model(Device))

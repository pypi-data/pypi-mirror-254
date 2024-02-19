from extras.plugins import PluginMenuButton
from extras.plugins import PluginMenuItem
from netbox.plugins import PluginMenu
from utilities.choices import ButtonColorChoices

sync_buttons = [
    PluginMenuButton(
        link="plugins:ipfabric_netbox:ipfabricsync_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        permissions=["add_ipfabricsync"],
        color=ButtonColorChoices.GREEN,
    )
]

source_buttons = [
    PluginMenuButton(
        link="plugins:ipfabric_netbox:ipfabricsource_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        permissions=["add_ipfabricsource"],
        color=ButtonColorChoices.GREEN,
    )
]

source = PluginMenuItem(
    link="plugins:ipfabric_netbox:ipfabricsource_list",
    link_text="Sources",
    buttons=source_buttons,
    permissions=["ipfabric_netbox.view_ipfabricsource"],
)

snapshot = PluginMenuItem(
    link="plugins:ipfabric_netbox:ipfabricsnapshot_list",
    link_text="Snapshots",
    permissions=["ipfabric_netbox.view_ipfabricsnapshot"],
)


ingestion = PluginMenuItem(
    link="plugins:ipfabric_netbox:ipfabricsync_list",
    link_text="Ingestion",
    buttons=sync_buttons,
    permissions=["ipfabric_netbox.view_ipfabricsync"],
)

tm = PluginMenuItem(
    link="plugins:ipfabric_netbox:ipfabrictransformmap_list",
    link_text="Transform Maps",
    permissions=["ipfabric_netbox.view_ipfabrictransformmap"],
    buttons=[
        PluginMenuButton(
            link="plugins:ipfabric_netbox:ipfabrictransformmap_add",
            title="Add",
            icon_class="mdi mdi-plus-thick",
            permissions=["ipfabric_netbox.add_ipfabrictransformmap"],
            color=ButtonColorChoices.GREEN,
        )
    ],
)
menu = PluginMenu(
    label="IP Fabric",
    icon_class="mdi mdi-cloud-sync",
    groups=(("IP Fabric", (source, snapshot, ingestion, tm)),),
)

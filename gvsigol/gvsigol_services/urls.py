from django.conf.urls import url

urlpatterns = [
    url(r'^workspace_list/$', 'gvsigol_services.views.workspace_list', name='workspace_list'),
    url(r'^workspace_add/$', 'gvsigol_services.views.workspace_add', name='workspace_add'),
    url(r'^workspace_import/$', 'gvsigol_services.views.workspace_import', name='workspace_import'),
    url(r'^workspace_delete/(?P<wsid>\d+)/$', 'gvsigol_services.views.workspace_delete', name='workspace_delete'),
    url(r'^datastore_list/$', 'gvsigol_services.views.datastore_list', name='datastore_list'),
    url(r'^datastore_add/$', 'gvsigol_services.views.datastore_add', name='datastore_add'),
    url(r'^datastore_update/(?P<datastore_id>[0-9]+)/$', 'gvsigol_services.views.datastore_update', name='datastore_update'),
    url(r'^datastore_delete/(?P<dsid>\d+)/$', 'gvsigol_services.views.datastore_delete', name='datastore_delete'),
    url(r'^backend_resource_list_available/$', 'gvsigol_services.views.backend_resource_list_available', name='backend_resource_list_available'),
    url(r'^layer_list/$', 'gvsigol_services.views.layer_list', name='layer_list'),
    url(r'^layer_add/$', 'gvsigol_services.views.layer_add', name='layer_add'),
    url(r'^layer_permissions/(?P<layer_id>[0-9]+)/$', 'gvsigol_services.views.layer_permissions_update', name='layer_permissions_update'),
    url(r'^get_resources_from_workspace/$', 'gvsigol_services.views.get_resources_from_workspace', name='get_resources_from_workspace'),
    url(r'^layer_update/(?P<layer_id>[0-9]+)/$', 'gvsigol_services.views.layer_update', name='layer_update'),
    url(r'^layer_delete/(?P<layer_id>[0-9]+)/$', 'gvsigol_services.views.layer_delete', name='layer_delete'),
    url(r'^cache_clear/(?P<layer_id>[0-9]+)/$', 'gvsigol_services.views.cache_clear', name='cache_clear'),
    url(r'^layergroup_cache_clear/(?P<layergroup_id>[0-9]+)/$', 'gvsigol_services.views.layergroup_cache_clear', name='layergroup_cache_clear'),
    url(r'^layer_upload/$', 'gvsigol_services.views.layer_upload', name='layer_upload'),
    url(r'^layer_create/$', 'gvsigol_services.views.layer_create', name='layer_create'),
    url(r'^get_geom_tables/(?P<datastore_id>[0-9]+)/$', 'gvsigol_services.views.get_geom_tables', name='geom_tables'),
    url(r'^layergroup_list/$', 'gvsigol_services.views.layergroup_list', name='layergroup_list'),
    url(r'^layergroup_add/$', 'gvsigol_services.views.layergroup_add', name='layergroup_add'),
    url(r'^layergroup_delete/(?P<lgid>[0-9]+)/$', 'gvsigol_services.views.layergroup_delete', name='layergroup_delete'),
    url(r'^layergroup_update/(?P<lgid>[0-9]+)/$', 'gvsigol_services.views.layergroup_update', name='layergroup_update'),
    url(r'^layer_boundingbox_from_data/$', 'gvsigol_services.views.layer_boundingbox_from_data', name='layer_boundingbox_from_data')
]
from django.conf.urls import url, include
from partenaire.api import PartenaireResource

part_res= PartenaireResource()

from geonode.urls import urlpatterns
from oca.views import HomePage

urlpatterns += [
## include your urls here
    url(r'^partenaire/', include('partenaire.urls')),
]

urlpatterns = [
   url(r'^/?$',
       HomePage.as_view(template_name='site_index.html'),
       name='home'),
] + urlpatterns

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from graphene_django.views import GraphQLView

from graphql_pokedex.schema import schema


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

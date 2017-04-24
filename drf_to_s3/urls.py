from django.conf.urls import url
from drf_to_s3.views import api_client_views, fine_uploader_views

urlpatterns = [
    url(r'^upload_uri$', api_client_views.SignedPutURIView.as_view()),
    url(r'^sign$', fine_uploader_views.FineSignPolicyView.as_view()),
    url(r'^success$', fine_uploader_views.FineUploadCompletionView.as_view()),
    url(r'^empty_html$', fine_uploader_views.empty_html),
]

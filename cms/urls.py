from django.urls import path

from cms.views import PageView

app_name = 'cms'

urlpatterns = [
    path('<str:page_slug>', PageView.as_view(), name='page'),
]

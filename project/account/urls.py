from django.urls import path
from .views import *

urlpatterns = [
    path('tlist',TodoListView.as_view(),name='tlist'),
    path('tadd',TodoaddView.as_view(),name="tadd"),
    path('tdel/<int:id>',TodoDeleteView.as_view(),name="tdel"),
    path('tedit/<int:id>',TodoEditView.as_view(),name="tedit"),
    

]
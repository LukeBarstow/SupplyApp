from django.urls import path

from . import views

app_name = 'supply'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:barracks_id>/', views.floor, name='floor'),
    path('<int:barracks_id>/<int:floor_id>', views.bathroom, name='bathroom'),
    path('<int:barracks_id>/<int:floor_id>/<int:bathroom_id>', views.statuses, name='statuses'),
    path('<int:barracks_id>/<int:floor_id>/<int:bathroom_id>/<int:item_id>', views.update, name='update'),
]

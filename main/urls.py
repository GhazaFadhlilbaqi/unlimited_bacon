from django.urls import path
from main.views import show_main, create_bacon_entry
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_product, delete_product
from main.views import add_product_entry_ajax
from main.views import create_product_entry_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_bacon_entry', create_bacon_entry, name='create_bacon_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit_product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('add-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('create-flutter/', create_product_entry_flutter, name='create_product_entry_flutter'),
]
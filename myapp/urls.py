from django.urls import path
from .views import *
 
urlpatterns = [
 
    path('', HomeView, name='home'),
    path('deletedata/', DeletedataView, name='deletedata'),
    path('databackup/', DataBackupView, name='databackup'),
    path('load_data/', LoadBackupView, name='load_data'),
    
    
    path('sqlLite_config/', SqlLiteconfigView, name='sqlLite_config'),
    path('db_config/', DatabaseConfigView, name='db_config'),

    path('mysql_config/', MysqlconfigView, name='mysql_config'),

    

]

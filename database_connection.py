from django.db import connections
from django.db.utils import OperationalError
db_conn = connections['default']

# ----------- Check database connecton status (connected or not) -----------
try:
    c = db_conn.cursor()
except OperationalError:
    connected = False
    # print(connected)
else:
    connected = True
    # print(connected)


# ----------- print database name -----------
from django.db import connection
db_name = connection.settings_dict['NAME']

# ----------- print database Vendor name -----------
from django.db import connection
db_vendor=connection.vendor








# ---------- Sqlite3 databse config ---------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# ---------- Postgresql databse config ---------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'test',
#         'USER': 'postgres',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# ---------- Mysql databse config ---------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'demo',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

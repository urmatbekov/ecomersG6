SECRET_KEY = 'osemb!qj9--mi%-8#oqh8fq3a-07ns0n@xfdscc6c6bd#%^yog'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['ecommerce-7-api.itpark.edu.kg']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grup_6',
        'USER': 'grup_6',
        'PASSWORD': 'Grup_98_6!',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

db_engine_map = {
    'postgres': 'django.db.backends.postgresql',
}

def parse_database_url(url):
    engine, uri = url.split('://', 1)
    credentials, db = uri.split('@', 1)
    user, password = credentials.split(':', 1)
    addr, name = db.split('/', 1)
    host, port = addr.split(':', 1)
    return {
        'ENGINE': db_engine_map[engine],
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
    }

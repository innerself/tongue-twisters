TORTOISE_SETTINGS = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '54321',
                'user': 'test',
                'password': 'test',
                'database': 'test',
            }
        },
    },
    'apps': {
        'tongue_twisters': {
            'models': ['backend.app.models', 'aerich.models'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        }
    }
}

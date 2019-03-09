import random
from aiohttp_app_boilerplate.utils import utc_now

async def health_check(request):
    ok_or_not_ok = bool(random.getrandbits(1))
    return {
        'health': 'OK',
        'data': {
            'third_party_service': 'OK' if ok_or_not_ok else 'FAIL'
        },
        'meta': {
            'generated_at': utc_now(),
            'product': 'Aiohttp App Boilerplate',
            'copyright': 'Copyright 2019 Yuvchenko, All Rights Reserved'
        }
    }, 200

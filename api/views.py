from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]

    return JsonResponse(routes, safe=False)
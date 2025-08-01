from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .services.staff.call_page import Call_Page
from .services.staff.interact_db import Interact_DB

def func_page(request, page):
    return Call_Page.get_page(request, page)

def interact_db(request, work):
    print('co vo')
    return Interact_DB.Run(request, work)

# @csrf_exempt
# def api_cap_nhat_trang_thai(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         id = data.get('id')
#         trang_thai = data.get('trang_thai')
#         try:
#             tg = ThamGia.objects.get(id=id)
#             tg.trang_thai = trang_thai
#             tg.save()
#             return JsonResponse({'success': True})
#         except ThamGia.DoesNotExist:
#             return JsonResponse({'error': 'Không tìm thấy'}, status=404)
#     return JsonResponse({'error': 'Sai method'}, status=400)


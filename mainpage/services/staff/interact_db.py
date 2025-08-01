from django.http import JsonResponse
import json

from .interact_DB.asignwork import Asign_Work
from .interact_DB.updatedata import Update_Data

from mainpage.models import Join

class Interact_DB:
    return_default = JsonResponse({'error': 'Không Lấy Được Thông Tin Nhân Viên'}, status=400)
    @staticmethod
    def Run(request, work):
        if request.method != 'POST':
            return JsonResponse({'error': 'Sai method'}, status=400)
        try:
            if work == 'asignWork':
                data = json.loads(request.body)
                role = data.get('role')
                id = data.get('id')
                change = data.get('change')
                return Asign_Work.Run(role, id, change)
            if work == 'updateData':
                data = json.loads(request.body)
                role = data.get('role')
                id = data.get('id')
                change = data.get('change')
                return Update_Data.Run(role, id, change)
            else:
                return Interact_DB.return_default
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Không Lấy Được Thông Tin Nhân Viên'}, status=400)
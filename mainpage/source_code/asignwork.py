from mainpage.models import Join

from django.http import JsonResponse
import json

class Asign_Work:
    @staticmethod
    def Coder(id, id_staf):
        try:
            j = Join.objects.get(id=id)
            j.id_staf=id_staf
            j.save()
            return JsonResponse({'success': True})
        except Join.DoesNotExist:
            return JsonResponse({'error': 'Không tìm thấy'}, status=404)
        
    @staticmethod
    def Run(request):
        if request.method != 'POST':
            return JsonResponse({'error': 'Sai method'}, status=400)
        try:
            data = json.loads(request.body)
            id = data.get('id')
            id_staf = data.get('id_staf')
            if 'ld_it' in data.get('role'):
                return Asign_Work.Coder(id, id_staf)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON lỗi'}, status=400)
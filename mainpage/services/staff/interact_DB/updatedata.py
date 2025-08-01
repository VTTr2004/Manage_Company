from mainpage.models import Join

from django.http import JsonResponse
import json

class Update_Data:
    @staticmethod
    def Coder(id, change):
        try:
            j = Join.objects.get(id=id)
            j.status=change
            j.save()
            return JsonResponse({'success': True})
        except Join.DoesNotExist:
            return JsonResponse({'error': 'Không Tìm Thấy Điều Kiện Thỏa (Coder)'}, status=404)
        
    @staticmethod
    def Run(role, id, change):
        try:
            if 'ld_it' in role:
                return Update_Data.Coder(id, change)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Lỗi Update_Data'}, status=400)
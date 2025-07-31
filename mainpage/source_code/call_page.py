from django.shortcuts import render, redirect

from mainpage.models import Account, Manage_Staf

from mainpage.source_code.func_class.infor import Infor
from mainpage.source_code.func_class.job import Job_Page

class Call_Page:
    @staticmethod
    def Check_Leader(access_token):
        id_staf = Account.objects.get(access_token=access_token).id_staf
        stafs = Manage_Staf.objects.filter(id_mana=id_staf)
        if len(stafs) != 0:
            return True
        return False

    def login(request):
        lg_page = 'login.html'
        if request.method == 'POST':
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()
            try:
                user = Account.objects.get(username=username, password=password)
            except Account.DoesNotExist:
                return render(request, lg_page, {'error': 'Sai thông tin đăng nhập.'})
            if user:
                # new_access_token = Create_Token()
                # user.access_token = new_access_token
                # request.session['access_token'] = new_access_token
                request.session['access_token'] = user.access_token
                return redirect('infor')
            else:
                return render(request, lg_page, {'error': 'Từ Chối Đăng Nhập.'})
        return render(request, lg_page)
    
    def logout(request):
        # token = request.session.get('access_token')
        # if token:
        #     try:
        #         user = Account.objects.get(access_token=token)
        #         user.access_token = ''
        #         user.save()
        #     except Account.DoesNotExist:
        #         pass
        request.session.flush()
        return redirect('login')
    
    def get_page(request, page):
        if page == 'login':
            return Call_Page.login(request)
        lead = Call_Page.Check_Leader(request.session['access_token'])
        if page == 'infor':
            addr, staf_content, staf_inf = Infor.Get_Data(request.session['access_token'],
                                                          leader = lead)
            return render(request, 'staff_page/func_page/base_infor.html', {
                'addr':addr,
                'staf_content':staf_content,
                'staf_inf':staf_inf
            })
        if page == 'job':
            staf_inf = Infor.Get_Data(request.session['access_token'], inf_only=True)
            addr, staf_content = Job_Page.Get_Data(request.session['access_token'],
                                                          leader = lead)
            return render(request, 'staff_page/func_page/base_job.html', {
                'addr':addr,
                'staf_content':staf_content,
                'staf_inf':staf_inf
            })
        if page == 'logout':
            return Call_Page.logout(request)
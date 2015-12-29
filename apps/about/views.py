# coding: utf-8
import subprocess

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from models import LeaveMessage
from ..common.functions import get_remote_ip_addr_by_request

@csrf_exempt
def index(request):
    """ 注册 """
    if request.method == 'GET':
        return render_to_response('about/index.html')


@csrf_exempt
def terminal(request):
    """ 注册 """
    if request.method == 'GET':
        return render_to_response('about/terminal.html')

    if request.method == 'POST':
        cmd = request.POST.get('cmd')
        if cmd not in settings.ALLOWED_CMD_A:
            return HttpResponse(u'禁止的命令!')
        else:
            s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            (stdoutdata, stderrdata) =  s.communicate()
            result = stdoutdata
            return HttpResponse(result)


@csrf_exempt
def leavemessage(request):
    """
    get:显示留言列表
    post: 提交留言
    """
    try:
        if request.method == 'GET':
            messages = LeaveMessage.objects.order_by('-id')
            return render_to_response('about/leavemessage.html', {'messages': messages})
        if request.method == 'POST':
            content = request.POST.get('message_content')
            ip = get_remote_ip_addr_by_request(request)
            if request.user.is_authenticated():
                t = LeaveMessage.objects.create(user=request.user, content=content, ip=ip)
            else:
                t = LeaveMessage.objects.create(content=content, ip=ip)
            return HttpResponse('ok')
    except Exception, e:
        print 'eeee:', e
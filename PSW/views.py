"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from PSW.forms import PswCreateForm, CommandForm
import paramiko
from subprocess import call
from PSW.models import Commands
from django.contrib.auth.models import User

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'psw/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'psw/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'psw/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def register(request):
    if request.method == 'POST':
        form = PswCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('poszło')
    form = PswCreateForm()
    return render(request, 'psw/register.html', {'form': form})

def servers(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['ip']
            system = form.cleaned_data['system']
            ram = form.cleaned_data['ram']
            quote = form.cleaned_data['quote']
            commandlog = 'python3.5 /root/log_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + ' >> PSW_log.log'
            command = 'python3.5 /root/main_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + '  > wyniki_testy.txt'            
            #form.save()
            #Tworzenie ze skryptu.py Python 3.5 
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('89.206.7.46', username='root', password='TrudneHaslo123')
                # Tworzenie Log
                stdin, stdout, stderr = ssh.exec_command(commandlog)
                # Tworzenie kontenerow
                stdin, stdout, stderr = ssh.exec_command(command)
                ssh.close()
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print ('Error %s' %e)
                return HttpResponseRedirect('servers/')
            return HttpResponseRedirect('/')
    else:
         form = CommandForm()
    return render(request, 'psw/servers.html', {'form': form})

def listservers(request):
    servers = Commands.objects.all
    context_dict = {'servers': servers}
    return render(request, 'psw/listservers.html' , context_dict)
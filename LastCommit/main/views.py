from django.shortcuts import render
import subprocess

def index(request):
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
    return render(request, 'main/index.html', {'commit':commit})


from django.shortcuts import render,redirect
from django.contrib import messages
from .models import StudentModel,AddmissionModel
from django.conf import settings
base_dir = settings.BASE_DIR
from datetime import datetime
from django.core.management import call_command
import os
from django.contrib.contenttypes.models import ContentType
from database_connection import db_vendor
def HomeView(request):
    all_students = StudentModel.objects.all()
   
    context = {'all_students':all_students,'db_vendor':db_vendor}
    return render(request,'index.html',context)

def DeletedataView(request):
    StudentModel.objects.all().delete()
    messages.error(request,'Students all data deleted')
    return redirect("/")

def DataBackupView(request):
    now = datetime.now()
    today_date = now.strftime("%d-%m-%y")
    today_time = now.strftime("(%I-%M-%p)")
    w= str(today_date+"_"+today_time)
    try:
        os.makedirs("Backup")
    except:
        pass
    directory = os.getcwd()
    p = os.path.join(directory,f"Backup\{w}.json")
    with open(p, "w", encoding="utf-8") as fp:
        call_command(f"dumpdata", format="json", indent=3, stdout=fp)
        messages.success(request,'Dabase backup success')
        return redirect('/')

def LoadBackupView(request):
    if request.method == "POST":
        ContentType.objects.all().delete() # require for datbase restore form one plateform to another ex: (sqlLite3 to Postgresql or Mysql)
        data_file = request.POST.get('data_file')
        f_path = os.path.join(base_dir,'Backup',data_file)
        call_command("loaddata",f_path)
        messages.info(request,'Dabase backup success')
        return redirect('/')
    else:
        return render(request,'index.html')


def DatabaseConfigView(request):
    if request.method == "POST":
        db_vendor = request.POST.get('db_vendor')
        db_name = request.POST.get('db_name')
        db_user = request.POST.get('db_user')
        db_pass = request.POST.get('db_pass')
        db_host = request.POST.get('db_host')
        db_port = request.POST.get('db_port')

        # Postgresql -----> database config
        if db_vendor == "3":
            file1 = open("ok.py", "w")
            L = [
            "DATABASES = { \n", 
            "    'default': { \n",
            "    'ENGINE': 'django.db.backends.postgresql_psycopg2', \n",
            f"    'NAME': '{db_name}', \n",
            f"    'USER': '{db_user}', \n",
            f"    'PASSWORD': '{db_pass}', \n",
            f"    'HOST': '{db_host}', \n",
            f"    'PORT': {int(db_port)}, \n",
            "    } \n",
            "  } \n",
            ]
            file1.writelines(L)
            file1.close()
            # time.sleep(1.3)
            import subprocess 
            subprocess.run('python manage.py migrate', shell=True)
            # subprocess.run('python manage.py runserver', shell=True)
            # import time
        
         
    return redirect("/")
    




# ============= Databaase config setup functions =======================

def Postgresql3configView(request):
    print("*************")
    file1 = open("ok.py", "w")
    L = [
    "from pathlib import Path \n"
    "BASE_DIR = Path(__file__).resolve().parent.parent \n"
    "\n"
    "\n"
    "# ---------- Postgresql databse config --------------- \n"
    "DATABASES = { \n", 
    "    'default': { \n",
    "    'ENGINE': 'django.db.backends.postgresql_psycopg2', \n",
    f"    'NAME': 'test', \n",
    f"    'USER': 'postgres', \n",
    f"    'PASSWORD': 'root', \n",
    f"    'HOST': 'localhost', \n",
    f"    'PORT': 5432, \n",
    "    } \n",
    "  } \n",
    ]
    file1.writelines(L)
    file1.close()
    import time
    time.sleep(1.3)
    # call_command("migrate")
    return redirect("/")


def MysqlconfigView(request):
    print("*************")
    file1 = open("ok.py", "w")
    L = [
    "from pathlib import Path \n"
    "BASE_DIR = Path(__file__).resolve().parent.parent \n"
    "\n"
    "\n"
    "# ---------- Mysql databse config --------------- \n"
    "DATABASES = { \n", 
    "    'default': { \n",
    "    'ENGINE': 'django.db.backends.mysql', \n",
    f"    'NAME': 'demo', \n",
    f"    'USER': 'root', \n",
    f"    'PASSWORD': 'root', \n",
    f"    'HOST': 'localhost', \n",
    f"    'PORT': 3306, \n",
    "    } \n",
    "  } \n",
    ]
    file1.writelines(L)
    file1.close()
    import time
    time.sleep(1.3)
    return redirect("/")

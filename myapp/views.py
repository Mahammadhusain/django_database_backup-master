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
import subprocess 
# ----- PostgreSQL using Psycopg2 -----
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# ----- Mysql using mysqlclient -----
import MySQLdb



def HomeView(request):
    try:
        all_students = StudentModel.objects.all()
        context = {'all_students':all_students,'db_vendor':db_vendor}
        return render(request,'index.html',context)
    except:
        messages.info(request,f'your are successfully switched ')
        print("^^^^^^^^^^^^^^^^^^^")
        return redirect("/")

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
        messages.info(request,'Dabase restore success')
        return redirect('/')
    else:
        return render(request,'index.html')


def DatabaseConfigView(request):
    if request.method == "POST":
        db_vendor = request.POST.get('db_vendor')
        print(db_vendor,"******")
        db_name = request.POST.get('db_name')
        db_user = request.POST.get('db_user')
        db_pass = request.POST.get('db_pass')
        db_host = request.POST.get('db_host')
        db_port = request.POST.get('db_port')

        # ------------------------------------------------------------
        

        # Connect to PostgreSQL DBMS
        con = psycopg2.connect(f"user={db_user} password={db_pass}");
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

        # Obtain a DB Cursor
        cursor = con.cursor();
        
        try:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
            
        except:
            print("hmmmmmmmmmmm...........")
            
        
        # ------------------------------------------------------------
        


        # Postgresql -----> database config
        if db_vendor == "3":
            file1 = open("serializerfieldsdoc/ok.py", "w")
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
            subprocess.run('python manage.py migrate', shell=True)
            messages.info(request,f'your are successfully switched ')
            return redirect("/")
    
    # return redirect("/")
    

def MysqlconfigView(request):
    if request.method == "POST":
        db_vendor = request.POST.get('db_vendor')
        db_name = request.POST.get('db_name')
        db_user = request.POST.get('db_user')
        db_pass = request.POST.get('db_pass')
        db_host = request.POST.get('db_host')
        db_port = request.POST.get('db_port')


        try:
            db = MySQLdb.connect(db_host,db_user,db_pass)
            cursor = db.cursor()
            cursor.execute(f"create database {db_name}")
        except:
            print("alredy 🙂🙂🙂🙂🙂🙂")

        # Mysql -----> database config
        if db_vendor == "2":
            file1 = open("serializerfieldsdoc/ok.py", "w")
            L = [
            "DATABASES = { \n", 
            "    'default': { \n",
            "    'ENGINE': 'django.db.backends.mysql', \n",
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
            subprocess.run('python manage.py migrate', shell=True)
            messages.info(request,f'your are successfully switched ')
            return redirect("/")


def SqlLiteconfigView(request):
    if request.method == "POST":
    # Mysql -----> database config
        import sqlite3
        # from django.conf import settings
        # value = settings.BASE_DIR
        # p =os.path.join(value,)
        file1 = open("serializerfieldsdoc/ok.py", "w")
        L = [
        "from pathlib import Path \n",
        "BASE_DIR = Path(__file__).resolve().parent.parent \n",
        "\n",
        "\n",
        "\n",
        "DATABASES = { \n", 
        "    'default': { \n",
        "    'ENGINE': 'django.db.backends.sqlite3', \n",
        f"    'NAME': BASE_DIR / 'db.sqlite3', \n",
        "    } \n",
        "  } \n",
        ]
        file1.writelines(L)
        file1.close()
        subprocess.run('python manage.py migrate', shell=True)
        messages.info(request,f'your are successfully switched ')
        return redirect("/")

from django.shortcuts import render
from django.http import HttpResponseRedirect
from mail import dbconnection
import random
import string
from datetime import date

# Create your views here.

def home(request):

     if request.POST.get('sub'):
          u=request.POST['em']
          ps=request.POST['ps']
          sql="select * from logdata where Userid='"+u+"' and Password='"+ps+"'"
          data=dbconnection.selone(sql)  
          if data:
               request.session['em']=u
           
               if data[3]=="User":
                    return HttpResponseRedirect('gmail')
          else:
              msg="please check your userid and password"
              return render(request,'home.html',{'b':msg})

     return render(request,"home.html",{}) 



        

# def regist1(request):
    
#      if request.POST.get('sub'):     
#           fn=request.POST['fn']
#           ln=request.POST['ln']
#           em=request.POST['us']
#           em=em+"@gmail.com"
#           pas=request.POST['ps'] 
#           sql='insert into registration(Firstname,Lastname,Username,Password) values("'+fn+'","'+ln+'","'+em+'","'+pas+'")'
#           dbconnection.addrow(sql)
#           sql="insert into logdata(Userid,Password,Utype) values('"+em+"','"+pas+"','User')"
#           dbconnection.addrow(sql)
          

#      return render(request,"regist1.html",{})


# def regist1(request):
#      if request.method=="POST":
#           fn=request.POST['fn']
#           ln=request.POST['ln']
#           em=request.POST['us']
#           em=em+"@gmail.com"
#           pas=request.POST['ps']
#           sql2='insert into registration(Firstname,Lastname,Username,Password) values("'+fn+'","'+ln+'","'+em+'","'+pas+'")'
#           dbconnection.addrow(sql2)
#           sql="insert into logdata(Userid,Password,Utype) values('"+em+"','"+pas+"','User')"           
#           dbconnection.addrow(sql)
          
#      return render(request,"regist1.html",{}) 






def gmail(request):
     t=date.today()
     em=request.session['em']
     sql="select * from compose order by senttime  DESC" 
     dbconnection.addrow(sql)
     sql="select * from compose where  inbox_delete='0' and Toname='"+em+"'and maildate='"+str(t)+"' "
     data=dbconnection.selall(sql)
     sql1="select * from compose where inbox_delete='0' and  Toname='"+em+"'"
     data1=dbconnection.selall(sql1)
     lst1=[]
     lst2=[]
     for i in data1:
          if i[7]==t:
               lst1.append(i)
          else:
               lst2.append(i) 
     return render(request,'gmail.html',{'d':lst1,'f':lst2,'h':data1}) 

def compose(request):
     if request.method=="POST":
          # From=request.POST['From']
          From=request.session['em']
          to=request.POST['to']
          sub=request.POST['sub']
          txt=request.POST['txt']
          sql="insert into compose(Fname,Toname,Subject,Content,Status,maildate,mailtime,sent_delete,inbox_delete,sent_star,inbox_star) values('"+From+"','"+to+"','"+sub+"','"+txt+"','0',curdate(),curtime(),'0','0','0','0')"
          dbconnection.addrow(sql) 
          return  HttpResponseRedirect('gmail')
     return render(request,'compose.html',{})

def sent(request):
     From=request.session['em']
     sql1="select * from logdata where Userid='"+From+"'"
     sql="select * from compose where sent_delete=0 and  Fname='"+From+"'"
     data1=dbconnection.selone(sql1)
     data=dbconnection.selall(sql)
     return render(request,'sent.html',{'b':data})

def smore(request):
     data=request.GET['sid']
     sql="select * from compose where id='"+data+"' "
     data1=dbconnection.selone(sql)
     if request.POST.get("forward"):
          r=request.POST.get('recepient')
          fc=request.POST.get('fc')
          t=date.today()
          sub=request.POST.get('sub')
          From=request.session['em']
          sql3="insert into compose(Fname,Toname,Subject,Content,Status,maildate,mailtime,sent_delete,inbox_delete,sent_star,inbox_star) values('"+From+"','"+r+"','"+sub+"','"+fc+"','0',curdate(),curtime(),'0','0','0','0')"
          dbconnection.addrow(sql3)
     if request.POST.get("reply"):
          r=request.POST.get('recepient')
          fc=request.POST.get('fc')
          t=date.today()
          sub=request.POST.get('sub')
          From=request.session['em']
          sql3="insert into compose(Fname,Toname,Subject,Content,Status,maildate,mailtime,sent_delete,inbox_delete,sent_star,inbox_star) values('"+str(From)+"','"+str(r)+"','"+str(sub)+"','"+str(fc)+"','0',curdate(),curtime(),'0','0','0','0')"
          dbconnection.addrow(sql3)
    
          sql1="select * from compose where sent_delete=0 and  Fname='"+From+"'"
          data7=dbconnection.selone(sql1)

         
          return HttpResponseRedirect('snt')
     return render(request,'smore.html',{'c':data1})


def inbox(request):
     t=date.today()
     em=request.session['em']
     sql="select * from compose order by senttime  DESC" 
     dbconnection.addrow(sql)
     sql="select * from compose where  inbox_delete='0' and Toname='"+em+"'and maildate='"+str(t)+"' "
     data=dbconnection.selall(sql)
     sql1="select * from compose where inbox_delete='0' and  Toname='"+em+"'"
     data1=dbconnection.selall(sql1)
     lst1=[]
     lst2=[]
     for i in data1:
          if i[7]==t:
               lst1.append(i)
          else:
               lst2.append(i)           
     return render (request,'inbox.html',{'d':lst1,'f':lst2,'h':data1})
     
def deldata(request):
     data=request.GET['id'] 
     em=request.session['em'] 
     sql="update compose set sent_delete='1' where id='"+data+"'"
     dbconnection.uprow(sql)
     return HttpResponseRedirect('snt')

def deldata1(request):
     data=request.GET['did']  
     sql="update compose set inbox_delete='1' where id='"+data+"'"
     dbconnection.uprow(sql)
     return HttpResponseRedirect('inbox')
          
def bin(request):
     em=request.session['em']
     sql1="select * from logdata where Userid='"+em+"'"
     data1=dbconnection.selone(sql1)
     sql="select * from compose where (Toname='"+em+"' and inbox_delete='1') OR(Fname='"+em+"' and sent_delete='1')"
     data=dbconnection.selall(sql)
     return render(request,'bin.html',{'e':data})


     

def inboxmore(request):
     data=request.GET['inid']
     sql="select * from compose where id='"+str(data)+"' "
     data1=dbconnection.selone(sql)
     if request.POST.get("forward"):
          r=request.POST.get('recepient')
          fc=request.POST.get('fc')
          t=date.today()
          sub=request.POST.get('sub')
          From=request.session['em']
          sql3="insert into compose(Fname,Toname,Subject,Content,Status,maildate,mailtime,sent_delete,inbox_delete,sent_star,inbox_star) values('"+From+"','"+r+"','"+sub+"','"+fc+"','0',curdate(),curtime(),'0','0','0','0')"
          dbconnection.addrow(sql3)
     if request.POST.get("reply"):
          r=request.POST.get('recepient')
          fc=request.POST.get('fc')
          t=date.today()
          sub=request.POST.get('sub')
          From=request.session['em']
          sql3="insert into compose(Fname,Toname,Subject,Content,Status,maildate,mailtime,sent_delete,inbox_delete,sent_star,inbox_star) values('"+str(From)+"','"+str(r)+"','"+str(sub)+"','"+str(fc)+"','0',curdate(),curtime(),'0','0','0','0')"
          dbconnection.addrow(sql3)
    
          sql1="select * from compose where sent_delete=0 and  Fname='"+From+"'"
          data7=dbconnection.selone(sql1)

         
          return HttpResponseRedirect('inbox')


     return render(request,'inboxmore.html',{'j':data1})

def stared(request):
     data=request.GET['id']  
     sql="update compose set inbox_star='1' where id='"+data+"'"
     dbconnection.uprow(sql)
     return HttpResponseRedirect('inbox')

def stared1(request):
     data=request.GET['id1']  
     sql="update compose set sent_star='1' where id='"+data+"'"
     dbconnection.uprow(sql)
     return HttpResponseRedirect('snt')

def stareds(request):
     em=request.session['em']
     sql="select * from compose where (Toname='"+em+"' and inbox_star='1') OR(Fname='"+em+"' and sent_star='1')"
     data=dbconnection.selall(sql)
     return render(request,'stared.html',{'k':data})


def mystard(request):
     data=request.GET['mid']  
     sql="update compose set inbox_star='3'  where id='"+data+"'"
     dbconnection.uprow(sql)
     sql4="update compose set sent_star='3'  where id='"+data+"'"
     dbconnection.uprow(sql4)
     return HttpResponseRedirect('strd')



def starmore(request):
     data=request.GET['stid']
     
     sql="select * from compose where id='"+data+"' "
     data1=dbconnection.selone(sql)
     return render(request,'starmore.html',{'q':data1})

def forward(request):
     
     data=request.GET['fid']
     sql="update compose set sent_frwd='1'  where id='"+data+"'"
     dbconnection.uprow(sql)
     return render(request,'smore.html',{})

def forwd(request):
     data=request.GET['fid']
     sql="select * from compose where id='"+data+"' "
     data1=dbconnection.selone(sql)
     
     return render(request,'starmore.html',{'h':data1})
     
     
def regist1(request):
    if request.POST.get('sub'):
        f=request.POST.get('fn')
        l=request.POST.get('ln')
        u=request.POST.get('us')
        u_name=u+'@gmail.com'
        p=request.POST.get('ps')
        sql2="select * from logdata where Userid='"+u_name+"'"
        data2=dbconnection.selall(sql2)
        if data2:
            msg="That username is taken.Try another."
            return render(request,"regist1.html",{'n':msg})

     
        else:
            sql1="insert into registrations(Firstname,Lastname,Username,Password)values('"+f+"','"+l+"','"+u_name+"','"+p+"')"
            dbconnection.addrow(sql1)
            sql="insert into logdata(Userid,Password,Utype) values('"+u_name+"','"+p+"','User')" 
            dbconnection.addrow(sql)         
            return render(request,"regist1.html",{})  
    return render(request,"regist1.html",{})
    
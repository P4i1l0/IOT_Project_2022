from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Tables
# Create your views here.

def index(request):
    tables = Tables.objects.all()
    context = {'tables': tables}
    return render(request,'myapp/index.html',context)

def level(request):
    html = '''
    <form action="/iot" method="GET">
        위치 title : <input type="text" name="title"><br>
        현재인원 : <input type="text" name="len_person"><br>
        최대인원 : <input type="text" name="max_person"><br>
        위도 : <input type="text" name="x"><br>
        경도 : <input type="text" name="y"><br>
        <input type="submit" value="입력">
    </form>
    '''
    return HttpResponse(html)

def iot(request):
    title  = request.GET.get('title')
    len_person  = int(request.GET.get('len_person'))
    max_person  = int(request.GET.get('max_person'))
    try:
        level = (len_person/max_person)*100
    except ZeroDivisionError:
        print('error 0')
        level = 0
    x  = request.GET.get('x')
    y  = request.GET.get('y')
    if len(Tables.objects.filter(x=x, y=y)) == 0:
        t = Tables(title=title, len_person=len_person, max_person=max_person, level=level, x=x, y=y)
        t.save()
    else:
        move = (Tables.objects.filter(x=x) & Tables.objects.filter(y=y))[0]
        move.title = title
        move.len_person = len_person
        move.max_person = max_person
        move.level = level
        move.x = x
        move.y = y
        move.save()

    return HttpResponse('OK')


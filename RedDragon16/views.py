from django.shortcuts import render
from .models import*
# Create your views here.
def Home(request):
    Database = {
        'posts':HomePost.objects.all()
    }
    return render(request, 'Home.html', Database)

def About(request):
    Database = {
        'posts':AboutPost.objects.all()
    }
    return render(request, 'About.html', Database)

def Music(request):
    MusicPost = [
        {
            'title':'Music',
            'title_1':'1.Có Chắc Yêu Là Đây !',
            'title_2':'2.Talk To You !',
        }
    ]
    Database = {
        'posts':MusicPost
    }
    return render(request, 'Music.html', Database)

def Coding(request):
    Database = {
        'posts':CodingPost.objects.all()
    }
    return render(request, 'Coding.html', Database)

def CodingBotChat(request):
    Introduction = '''
    Hello các bạn , bây h chúng ta sẽ lập trình 1 con bot chat AI chỉ với Python nhé !
    '''
    MusicPost = [
        {
            'title':'CodingBotChat',
            'Introduction':Introduction,
            'title_1':'Bước 1: lập trình phần đăng nhập tên !',
            'title_2':'Bước 2: lập trình phần câu hỏi !',
            'title_3':'Bước 3: lập trình phần vòng lặp câu hỏi !',
            'title_4':'Bước 4: lập trình phần câu hỏi chưa update !',
            'title_5':'Bước 5: lập trình phần kết thúc !',
        }
    ]
    Database = {
        'posts':MusicPost
    }
    return render(request, 'CodingBotChat.html', Database)

def CodingWebDjango(request):
    Introduction = '''
    Hello các bạn , bây h chúng ta sẽ lập trình web Django nhé ! Đầu tiên chúng ta
    sẽ lập trình web Hello World !
    '''
    CodingWebDjangoPost = [
        {
            'title':'CodingWebDjango',
            'Introduction':Introduction,
            'title_1':'Bước 1: khởi tạo project !',
            'title_2':'Bước 2: tạo webapp Home !',
            'title_3':'Bước 3: settings webapp vào folder chính !',
            'title_4':'Bước 4: tạo url cho webapp !',
            'title_5':'Bước 5: tạo file urls.py trong webapp !',
            'title_6':'Bước 6: code file views !',
            'title_7':'Bước 7: code file urls !',
            'title_8':'Bước 8: tạo file runserver và chạy server !',
            'Result':'Hãy nhìn kết quả !',
        }
    ]
    Database = {
        'posts':CodingWebDjangoPost
    }
    return render(request, 'CodingWebDjango.html', Database)

def CodingWebDjango_1(request):
    Introduction = '''
    Hello các bạn , bây h chúng ta sẽ típ túc series lập trình web Django , hôm nay mik sẽ hướng dẫn các bạn
    tạo file folder templates rồi cho file HTML vào rồi code HTML !
    '''
    CodingWebDjango_1_Post = [
        {
            'title':'CodingWebDjango_1',
            'Introduction':Introduction,
            'title_1':'Bước 1: tạo folder templates trong app Home !',
            'title_2':'Bước 2: tạo file HTML !',
            'title_3':'Bước 3: khai báo file HTML ở bên views !',
            'title_4':'Bước 4: code file HTML !',
            'Result':'Nhìn kết quả !',
        }
    ]
    Database = {
        'posts':CodingWebDjango_1_Post
    }
    return render(request, 'CodingWebDjango_1.html', Database)

def CodingWebDjango_2(request):
    Introduction = '''
    Hello các bạn, hôm nay chúng ta típ tục series code web Django nhé, lần trước chúng ta có 1 cái web
    trong đó nó có HTML rồi , nhưng trông nó rất thô, nên để cho nó đẹp hơn thì ta cần CSS nên hôm nay chúng ta
    sẽ học cách tạo file static rồi cho CSS vào đó để code nhé !
    ''' 
    CodingWebDjango_2_Post = [
        {
            'title':'CodingWebDjango_2',
            'Introduction':Introduction,
            'title_1':'Bước 1: chỉnh sửa file settings.py trong folder chính !',
            'title_2':'Bước 2: tạo folder static và tạo folder CSS và tạo thêm file CSS !',
            'title_3':'Bước 3: khai báo file CSS trong HTML !',
            'title_4':'Bước 4: code menu trong HTML !',
            'title_5':'Bước 5: code CSS cho menu !',
            'Result':'Hãy nhìn kết quả !',
        }
    ]
    Database = {
        'posts':CodingWebDjango_2_Post
    }
    return render(request, 'CodingWebDjango_2.html', Database)

def CodingWebDjango_3(request):
    Introduction = '''
    Hello các bạn, típ tục series code web Django, hôm nay chúng ta sẽ học cách viết blog và
    cách nhúng ảnh nhé !
    '''
    CodingWebDjango_3_Post = [
        {
            'title':'CodingWebDjango_3',
            'Introduction':Introduction,
            'Big_Title':'1.Viết blog !',
            'title_1':'Bước 1: code file views như sau !',
            'title_2':'Bước 2: code file HTML như sau !',
            'title_3':'Bước 3: code thêm 1 chút CSS !',
            'Result_1':'Hãy nhìn kết quả đầu tiên !',
            'Big_Title_1':'2.Nhúng ảnh theo kiểu Django !',
            'title_1':'Bước 1: tạo file img trong folder static và lưu 1 file ảnh trong đó !',
            'title_2':'Bước 2: nhúng ảnh vào web HTML theo cách của Django !',
            'Result_2':'Hãy nhìn kết quả cuối !',
        }
    ]
    Database = {
        'posts':CodingWebDjango_3_Post
    }
    return render(request, 'CodingWebDjango_3.html', Database)
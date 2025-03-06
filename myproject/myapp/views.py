from django.shortcuts import render, HttpResponse
import random

#딕서너리를 그룹핑하기 좋은 리스트로 담는다
topics= [
    {'id':1, 'title':'routing', 'body':'Routing is...'},
    {'id':2, 'title':'view', 'body':'view is...'},
    {'id':3, 'title':'model', 'body':'model is...'},
    #딕서너리 정보구조에 li태그의 정보를 담는다.
]

#html코드를 함수화 시키기
def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>
    </html>              
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request,id):
    return HttpResponse('Read'+ id)

def create(request):
    return HttpResponse('Create')


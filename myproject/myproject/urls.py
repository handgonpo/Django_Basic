# http://127.0.0.1/  어떤 경로도 없다면 home이다.
# http://127.0.0.1/app

# http://127.0.0.1/create/ 데이터를 생성하는 페이지로 연결
# http://127.0.0.1/read/1/ 특정 데이터(id=1)를 읽는 페이지

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #장고에서 기본적으로 가지고 있는 관리자화면으로 이동하기 위한 라우팅 설정
    path('', include('myapp.urls'))  # 기본 경로("")로 들어오면 생성한 myapp 앱의 urls.py를 사용
]

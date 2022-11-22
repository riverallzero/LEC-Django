# Django
2022 응용소프트웨어개발 장고 프로젝트

### 1. 환경 설정
- Virtualenv 환경으로 가상환경 만들기
- Django 라이브러리 3.2.15 버전 설치

### Terminal
- 장고 설치 테스트
```commandline
python
import django
print(django.__version__)
```
- 서버 실행
```commandline
python manage.py runserver
```
- 관리자 계정 만들기
```commandline
python manage.py migrate
python manage.py createsuperuser
```
  
### 2. 모델 수정을 하면 Migrate를 하고 runserver를 해야함
```commandline
python manage.py makemigrations
python manage.py migrate
```

### 3. 터미널에서 admin페이지 확인하기(shell)
```commandline
>>> python manage.py shell

>>> from blog.models import Post, Category
>>> Post.objects.count()
6
>>> for p in Post.objects.all():
...     print(p)
...
[1] 안녕하시렵니까 :: riverallzero
[2] 두번째글 :: riverallzero
[3] 하이 :: riverallzero
[4] iphone 14 pro :: riverallzero
[5] 수업시간이네요 :: riverallzero
[6] 글 쓰기 :: riverallzero
```
### 4. shell plus 이용
```commandline
pip install django_extensions ipython
python manage.py shell_plus

In [2]: from blog.models import Post, Category

In [3]: Post.objects.count()
Out[3]: 6

In [4]: for p in Post.objects.all():
   ...:     print(p)
   ...: 
[1] 안녕하시렵니까 :: riverallzero
[2] 두번째글 :: riverallzero
[3] 하이 :: riverallzero
[4] iphone 14 pro :: riverallzero
[5] 수업시간이네요 :: riverallzero
[6] 글 쓰기 :: riverallzero

# category 추가하기
In [5]: cate_ag = Category.objects.create(name="스마트팜", slug="sfarm")

In [6]: cate_ag
Out[6]: <Category: 스마트팜>

In [7]: Category.objects.count()
Out[7]: 3
In [8]: Category.objects.all()
Out[8]: <QuerySet [<Category: 문화 & 예술>, <Category: 일상>, <Category: 스마트팜>]>
```

## Error 해결법
Error 명 | django.db.utils.OperationalError: no such table: blog_post
```text
python manage.py migrate --run-syncdb
```

## TDD (GitHub link)
https://github.com/saintdragon2/do_it_django_a_to_z/commits/master/blog/tests.py
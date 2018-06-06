from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'polls'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('ctime/', views.ctime, name='ctime'),
    path('num/', views.num, name='num'),
    path('show/<int:num>/<str:aaa>/', views.show, name='show'),
    path('use_template/<str:aaa>/', views.use_template, name='use_template'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('xzt/', views.Xzt, name='xzt'),
    path('xzt_index/', views.Xzt_index, name='xzt_index'),
    path('test/xzt_index/', views.Xzt_index, name='xzt_index'),
    path('xzt_index/xzt/', views.Xzt, name='xzt_index'),
    path('test/', views.Test, name='test'),
    path('test1/', views.Test1, name='test1'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#print(settings.STATIC_URL,"    ", settings.STATIC_ROOT)
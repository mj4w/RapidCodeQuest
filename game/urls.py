from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('quiz/',views.quiz,name='quiz'),
    path('signup/',views.signup_required, name='signup'),
    path('login/',views.login_required, name='login'),
    path('logout/',views.log_out, name='logout'),
    path('result/',views.result, name='result'),
    path('overall/<int:pk>/',views.overall_result,name='overall-result'),
    path('quiz/<str:choice>/',views.questions, name='questions'),
    # practice q
    path('practice/',views.practice_q, name='practice-q'),
    #leaderboard
    path('leaderboard/',views.leaderboards, name='leaderboards'),
    
    

 
  
]
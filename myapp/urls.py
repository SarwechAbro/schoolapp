from django.urls import path
from . import views


urlpatterns = [
    path('teacherapiview/', views.TeacherLRViewAPI.as_view(), name='teacherapiview'),
    path('teacherapiview/<int:pk>/', views.TeacherLRViewAPI.as_view(), name='teacherapiview'),
    path('teacherapi/<int:pk>/', views.TeacherAPI.as_view(), name='teacherapi'),

    path('studentapiview/', views.StudentLRViewAPI.as_view(), name='studentapiview'),
    path('studentapiview/<int:pk>/', views.StudentLRViewAPI.as_view(), name='studentapiview'),
    path('studentapi/<int:pk>/', views.StudentAPI.as_view(), name='studentapi'),

    path('classapiview/', views.ClassLRViewAPI.as_view(), name='classapiview'),
    path('classapiview/<int:pk>/', views.ClassLRViewAPI.as_view(), name='classapiview'),
    path('classapi/<int:pk>/', views.ClassAPI.as_view(), name='classapi'),

    path('chapterapiview/', views.ChapterLRViewAPI.as_view(), name='chapterapiview'),
    path('chapterapiview/<int:pk>/', views.ChapterLRViewAPI.as_view(), name='chapterapiview'),
    path('chapterapi/<int:pk>/', views.ChapterAPI.as_view(), name='chapterapi'),

    path('lectureapiview/', views.LectureLRViewAPI.as_view(), name='lectureapiview'),
    path('lectureapiview/<int:pk>/', views.LectureLRViewAPI.as_view(), name='lectureapiview'),
    path('lectureapi/<int:pk>/', views.LectureAPI.as_view(), name='lectureapi'),

    path('courseapiview/', views.CourseLRViewAPI.as_view(), name='courseapiview'),
    path('courseapiview/<int:pk>/', views.CourseLRViewAPI.as_view(), name='courseapiview'),
    path('courseapi/<int:pk>/', views.CourseAPI.as_view(), name='courseapi'),

]
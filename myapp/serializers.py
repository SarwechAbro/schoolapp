from rest_framework import serializers
from .models import Teacher, Student, Class, Course, Chapter, Lecture

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'        



class TeacherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Teacher 
        fields = '__all__'        



class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Lecture 
        fields = '__all__'        
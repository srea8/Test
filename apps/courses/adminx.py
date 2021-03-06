# _*_ coding:utf-8 _*_

__author__ = 'srea'
__date__ = '2018/06/01 14:07'

import xadmin

from .models import Course,Lesson,Video,CourseResource

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_num','add_time']
    search_fields =['name','desc','detail','degree','learn_times','students','fav_nums','image','click_num']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_num','add_time']

class LessonAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course__name', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'lesson__name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name','download' ,'add_time']
    search_fields = ['course', 'name','download']
    list_filter = ['course', 'name','download' ,'add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

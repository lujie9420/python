# @ Time    : 2019/9/23 21:52
# @ Author  : JuRan

import xadmin

from apps.courses.models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_time', 'students']
    search_fields = ['name', 'desc', 'degree', 'students']
    list_filter = ['name', 'desc', 'degree', 'learn_time', 'teacher__name', 'students']
    list_editable = ['degree', 'desc']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    list_editable = ['name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    list_editable = ['name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']




xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
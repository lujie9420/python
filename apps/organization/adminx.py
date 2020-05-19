# @ Time    : 2019/9/23 21:57
# @ Author  : JuRan
import xadmin

from apps.organization.models import Teacher,CourseOrg,City


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year','work_company']
    search_fields = ['org', 'name', 'work_year','work_company']
    list_filter = ['org', 'name', 'work_year','work_company']


class CourseOrgAdmin(object):
    list_display = ['name', 'click_nums', 'desc', 'fav_nums']
    search_fields = ['name', 'click_nums', 'desc', 'fav_nums']
    list_filter = ['name', 'click_nums', 'desc', 'fav_nums']


class CityAdmin(object):
    # 列表页面显示的字段
    list_display = ['id','name','desc']
    # 搜索的字段
    search_fields = ['name','desc']
    # 过滤字段
    list_filter = ['name','desc']
    # 修改字段
    list_editable = ['name','desc']


xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(City,CityAdmin)

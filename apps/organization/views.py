from django.shortcuts import render
from django.views import View
from apps.organization.models import CourseOrg,City
from django.shortcuts import render_to_response
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

class OrgView(View):
    def get(self,request):
        Orgs_list = CourseOrg.objects.all()
        Citys_list = City.objects.all()
        hot_course = Orgs_list.order_by('-click_nums')[:4]

        #通过机构类型对机构进行筛选
        #从网页中获取ct,如果没有获取则显示为空
        catgory = request.GET.get('ct','')
        if catgory:
            Orgs_list = Orgs_list.filter(category=catgory)

        city_id = request.GET.get('city','')
        if city_id:
            Orgs_list = Orgs_list.filter(city=city_id)

        #根据学习人数、课程数进行排序
        sort = request.GET.get('sort','')
        if sort == 'students':
            Orgs_list = Orgs_list.order_by('-students')
        elif sort == 'courses':
            Orgs_list = Orgs_list.order_by('-course_nums')

        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        #对课程机构进行分页
        p = Paginator(Orgs_list,per_page=3,request=request)

        orgs = p.page(page)

        content = {
            'Orgs_list': orgs,
            'Citys_list': Citys_list,
            'category':catgory,
            'city_id':city_id,
            'sort':sort,
            'hot_clicks':hot_course,
        }


        return render(request,'org-list.html',context=content)
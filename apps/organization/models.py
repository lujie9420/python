from django.db import models
from apps.courses.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name='城市')
    desc = models.CharField(max_length=20, verbose_name='描述')

    class Meta:
        verbose_name = '机构城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    tag = models.CharField(default='全国知名', max_length=10, verbose_name='机构标签')
    category = models.CharField(verbose_name='机构类别', max_length=4,
                                choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')))
    click_nums = models.IntegerField(verbose_name='点击数量', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数量', default=0)
    # 图片路径  /media/org/2019/9/django.jpg
    image = models.ImageField(verbose_name='机构图片', upload_to='org/%Y/%m', max_length=200)
    address = models.CharField(verbose_name='机构地址', max_length=150)
    students = models.IntegerField(verbose_name='学习人数', default=0)
    course_nums = models.IntegerField(verbose_name='课程数量', default=0)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='所在城市')

    is_auth = models.BooleanField(default=False,verbose_name='是否认证')
    is_gold = models.BooleanField(default=False,verbose_name='是否金牌')

    def courses(self):
        # [1: 2] 数据库查询结果切片 相当于limt  course_set Courses 类名
        courses = self.course_set.filter(is_classics=True)[1:2]
        return courses
    class Meta:

        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Teacher(BaseModel):
    org = models.ForeignKey('CourseOrg', on_delete=models.CASCADE, verbose_name='所属机构')
    name = models.CharField(verbose_name='老师名字', max_length=50)
    work_year = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(verbose_name='就职公司', max_length=20)
    points = models.CharField(verbose_name='教学特点', max_length=50)
    click_nums = models.IntegerField(verbose_name='点击数量', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数量', default=0)
    age = models.IntegerField(verbose_name='年龄', default=18)
    image = models.ImageField(verbose_name='头像', upload_to='teacher/%Y/%m', max_length=200)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
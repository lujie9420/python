from django.db import models

# Create your models here.

class BaseModel(models.Model):
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    class Meta:
        abstract = True

class Course(BaseModel):

    teacher = models.ForeignKey('organization.Teacher',on_delete=models.CASCADE,verbose_name='讲师',null=True)
    course_org = models.ForeignKey('organization.CourseOrg',on_delete=models.CASCADE,verbose_name='课程机构',null=True)
    name = models.CharField(max_length=20,verbose_name='课程名字')
    desc = models.CharField(max_length=300,verbose_name='课程描述')
    learn_time = models.IntegerField(default=0,verbose_name='课程时长')
    degree = models.CharField(choices=(('cj','初级'),('zj','中级'),('gj','高级')),verbose_name='难度',max_length=4)
    students = models.IntegerField(verbose_name='学习人数',default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数',default=0)
    click_nums = models.IntegerField(default=0,verbose_name='点击数量')
    category = models.CharField(default='后端开发',verbose_name='课程分类',max_length=20)
    tag = models.CharField(default="",verbose_name='课程标签',max_length=10)
    you_know = models.CharField(max_length=200,verbose_name='课程须知')
    teacher_tell = models.CharField(max_length=80,verbose_name='老师告诉你')
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(upload_to='course/%Y/%m',verbose_name='课程封面')

    is_classics = models.BooleanField(default=False,verbose_name='是否经典')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name

class Lesson(BaseModel):
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    name  = models.CharField(max_length=20,verbose_name='章节名字')

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name

class Video(BaseModel):
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='视频名称')
    learn_time = models.IntegerField(default=0, verbose_name='视频时长')
    url = models.CharField(max_length=200, verbose_name='视频URL')

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name

class CourseResource(BaseModel):
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='资料名称')
    file = models.FileField(upload_to='course/%Y/%m',max_length=200, verbose_name='下载地址')

    class Meta:
        verbose_name = '课程资料'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name



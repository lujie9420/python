from django.db import models
from apps.courses.models import BaseModel


class UserAsk(BaseModel):
    name = models.CharField(max_length=20,verbose_name='姓名')
    mobile = models.CharField(max_length=11,verbose_name='手机')
    course_name = models.CharField(max_length=50,verbose_name='课程名字')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(BaseModel):
    user = models.ForeignKey('users.UserProfile',on_delete=models.CASCADE,verbose_name='用户')
    course = models.ForeignKey('courses.Course',on_delete=models.CASCADE,verbose_name='课程')
    comments = models.CharField(max_length=200,verbose_name='课程')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(BaseModel):
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, verbose_name='用户')
    fav_id = models.IntegerField(verbose_name='数据Id')
    fav_type = models.IntegerField(choices=((1,'课程'),(2,'课程机构'),(3,'讲师')),verbose_name='收藏类型')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(BaseModel):
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, verbose_name='用户')
    message = models.CharField(max_length=200,verbose_name='消息内容')
    has_read = models.BooleanField(default=False,verbose_name='是否已读')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(BaseModel):
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='课程')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


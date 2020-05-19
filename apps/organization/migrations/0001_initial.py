# Generated by Django 2.2.4 on 2020-04-21 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('name', models.CharField(max_length=20, verbose_name='城市')),
                ('desc', models.CharField(max_length=20, verbose_name='描述')),
            ],
            options={
                'verbose_name': '机构城市',
                'verbose_name_plural': '机构城市',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', models.TextField(verbose_name='机构描述')),
                ('tag', models.CharField(default='全国知名', max_length=10, verbose_name='机构标签')),
                ('category', models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], max_length=4, verbose_name='机构类别')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数量')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数量')),
                ('image', models.ImageField(max_length=200, upload_to='org/%Y/%m', verbose_name='机构图片')),
                ('address', models.CharField(max_length=150, verbose_name='机构地址')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('course_nums', models.IntegerField(default=0, verbose_name='课程数量')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.City', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '课程机构',
                'verbose_name_plural': '课程机构',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='老师名字')),
                ('work_year', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=20, verbose_name='就职公司')),
                ('points', models.CharField(max_length=50, verbose_name='教学特点')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数量')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数量')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('image', models.ImageField(max_length=200, upload_to='teacher/%Y/%m', verbose_name='头像')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]
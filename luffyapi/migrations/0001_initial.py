# Generated by Django 2.0.7 on 2018-12-29 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='章节名')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='课程名')),
                ('image', models.CharField(max_length=32, verbose_name='课程图片')),
                ('level', models.SmallIntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], default=1, verbose_name='难度')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why', models.CharField(max_length=32, verbose_name='为什么报课程')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='luffyapi.Course', verbose_name='课程')),
                ('recommend_courses', models.ManyToManyField(related_name='re_course', to='luffyapi.Course', verbose_name='相关推荐课程')),
            ],
        ),
    ]
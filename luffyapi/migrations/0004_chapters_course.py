# Generated by Django 2.0.7 on 2018-12-29 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luffyapi', '0003_auto_20181229_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='luffyapi.Course', verbose_name='课程'),
            preserve_default=False,
        ),
    ]

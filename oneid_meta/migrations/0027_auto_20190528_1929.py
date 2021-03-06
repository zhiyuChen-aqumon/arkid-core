# Generated by Django 2.0.7 on 2019-05-28 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0026_managergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_boss',
            field=models.BooleanField(default=False, verbose_name='是否为主管理员'),
        ),
        migrations.AlterField(
            model_name='managergroup',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager_group', to='oneid_meta.Group'),
        ),
    ]

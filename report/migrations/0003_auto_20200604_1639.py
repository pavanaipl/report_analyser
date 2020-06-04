# Generated by Django 2.2.11 on 2020-06-04 11:09

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0002_usersdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersdetails',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='usersdetails',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='login',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='password',
        ),
        migrations.AddField(
            model_name='usersdetails',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default='1', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersdetails',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]

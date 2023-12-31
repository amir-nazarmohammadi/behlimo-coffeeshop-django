# Generated by Django 3.1 on 2023-05-07 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0003_auto_20230411_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('message', models.TextField(verbose_name='متن')),
                ('is_active', models.BooleanField(blank=True, null=True, verbose_name='فعال / غیرفعال')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='menu.menu', verbose_name='آیتم منو')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
            },
        ),
    ]

# Generated by Django 4.2 on 2023-05-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_contact_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='inconnu', max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('First_Name', models.CharField(default='inconnu', max_length=100)),
                ('Last_Name', models.CharField(default='inconnu', max_length=100)),
                ('Phone_Number', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
    ]

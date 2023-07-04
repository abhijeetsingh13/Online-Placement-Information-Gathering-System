# Generated by Django 4.0.3 on 2022-03-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_alumni_list_of_stud_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_username', models.EmailField(max_length=254)),
                ('alum_username', models.EmailField(max_length=254)),
                ('Sender', models.CharField(max_length=1)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('chat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Subject', models.CharField(default='Alert', max_length=40)),
                ('Notification', models.TextField()),
            ],
        ),
    ]
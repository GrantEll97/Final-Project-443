# Generated by Django 3.1.3 on 2020-11-20 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursedetails',
            old_name='CourseId',
            new_name='IdCourse',
        ),
    ]

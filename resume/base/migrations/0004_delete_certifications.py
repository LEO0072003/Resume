# Generated by Django 4.1.3 on 2022-11-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_milestones_certifications_certifications'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certifications',
        ),
    ]
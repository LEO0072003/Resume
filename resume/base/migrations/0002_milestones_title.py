# Generated by Django 4.1.3 on 2022-11-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestones',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

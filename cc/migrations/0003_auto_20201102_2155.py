# Generated by Django 3.1.1 on 2020-11-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0002_template'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='template',
            new_name='body',
        ),
        migrations.AddField(
            model_name='template',
            name='subject',
            field=models.CharField(default='All purpose', max_length=100),
        ),
    ]
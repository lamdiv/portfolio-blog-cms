# Generated by Django 3.1.5 on 2021-01-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210116_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='techonologies',
            new_name='technologies',
        ),
        migrations.RenameField(
            model_name='projecttechnology',
            old_name='technology',
            new_name='title',
        ),
    ]

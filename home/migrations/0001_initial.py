# Generated by Django 3.1.5 on 2021-01-16 09:52

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('thumbnail', models.ImageField(upload_to='project/thumbnail')),
                ('images', models.FileField(blank=True, upload_to='project/images/')),
                ('github', models.URLField(blank=True, null=True)),
                ('tag', models.CharField(choices=[('p', 'Personal'), ('b', 'Client')], max_length=1)),
                ('preview', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('technologies', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
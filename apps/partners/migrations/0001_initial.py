# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import cms.apps.media.models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_file_alt_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_online', models.BooleanField(default=True, help_text="Uncheck this box to remove the page from the public website. Logged-in admin users will still be able to view this page by clicking the 'view on site' button.", verbose_name='online')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=140, null=True, blank=True)),
                ('website', models.CharField(max_length=140, null=True, blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('logo', cms.apps.media.models.ImageRefField(related_name='+', on_delete=django.db.models.deletion.PROTECT, to='media.File')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]

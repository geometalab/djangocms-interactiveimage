# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cms.models.pluginmodel
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractiveImage',
            fields=[
                ('cmsplugin_ptr',
                 models.OneToOneField(primary_key=True, to='cms.CMSPlugin', serialize=False, parent_link=True,
                                      auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50, default='')),
                ('image',
                 models.ImageField(verbose_name='Image', upload_to=cms.models.pluginmodel.get_plugin_media_path,
                                   default='NULL')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='InteractivePoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=50, default='')),
                ('description', models.TextField(verbose_name='Description', default='')),
                ('xCoordinate', models.IntegerField(default=0)),
                ('yCoordinate', models.IntegerField(default=0)),
                ('interactiveimage', models.ForeignKey(null=True, to='interactive_image_plugin.InteractiveImage')),
                ('pages', models.ManyToManyField(blank=True, verbose_name='Pages', to='cms.Page', related_name='pages',
                                                 null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

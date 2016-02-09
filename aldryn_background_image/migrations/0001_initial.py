# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(help_text='Optional label for this plugin.', max_length=128, verbose_name='label', blank=True)),
                ('id_name', models.CharField(max_length=50, verbose_name='id name', blank=True)),
                ('tag_type', models.CharField(default='div', max_length=50, verbose_name='tag Type', choices=[('div', 'div'), ('header', 'header'), ('footer', 'footer'), ('article', 'article'), ('section', 'section')])),
                ('background_repeat', models.CharField(default='repeat', max_length=128, null=True, blank=True, choices=[('repeat', 'repeat'), ('repeat-x', 'repeat-x'), ('repeat-y', 'repeat-y'), ('no-repeat', 'no-repeat'), ('initial', 'initial'), ('inherit', 'inherit')])),
                ('background_position', models.CharField(max_length=128, null=True, blank=True)),
                ('background_size', models.CharField(help_text='auto|length|cover|contain|initial|inherit', max_length=128, null=True, blank=True)),
                ('additional_class_names', models.TextField(help_text='Comma separated list of additional classes to apply to tag_type', verbose_name='additional classes', blank=True)),
                ('background_image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, to='filer.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

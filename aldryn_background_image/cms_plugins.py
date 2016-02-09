# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import BackgroundImage


class BackgroundImagePlugin(CMSPluginBase):
    model = BackgroundImage
    name = _("Background Image")
    render_template = "aldryn_background_image/plugin.html"
    allow_children = True

    fieldsets = (
        (None, {
            'fields': ('background_image', 'tag_type', )
        }),
        (_('Advanced Settings'), {
            'classes': ('collapse',),
            'fields': (
                'background_repeat',
                'background_position',
                'background_size',
                'additional_class_names',
                'label',
                'id_name',
            ),
        }),
    )

plugin_pool.register_plugin(BackgroundImagePlugin)

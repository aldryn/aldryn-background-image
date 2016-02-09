# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')

@python_2_unicode_compatible
class BackgroundImage(CMSPlugin):
    """
    A django CMS Plugin to change background images
    """

    TAG_TYPE_CHOICES = (
        ('div', 'div'),
        ('header', 'header'),
        ('footer', 'footer'),
        ('article', 'article'),
        ('section', 'section'),
    )
    BACKGROUND_REPEAT_CHOICES = (
        ('repeat', 'repeat'),
        ('repeat-x', 'repeat-x'),
        ('repeat-y', 'repeat-y'),
        ('no-repeat', 'no-repeat'),
        ('initial', 'initial'),
        ('inherit', 'inherit'),
    )

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin, related_name='+', parent_link=True)

    label = models.CharField(_('label'), max_length=128, blank=True,
                             help_text=_('Optional label for this plugin.'))
    id_name = models.CharField(_('id name'), max_length=50, blank=True)
    tag_type = models.CharField(
        verbose_name=_('tag Type'), max_length=50, choices=TAG_TYPE_CHOICES,
        default=TAG_TYPE_CHOICES[0][0])
    background_image = FilerImageField(null=True, on_delete=models.SET_NULL)
    background_repeat = models.CharField(
            max_length=128, blank=True, null=True, default=BACKGROUND_REPEAT_CHOICES[0][0],
            choices=BACKGROUND_REPEAT_CHOICES)
    background_position = models.CharField(max_length=128, blank=True,
                                           null=True)
    background_size = models.CharField(
            max_length=128, blank=True, null=True,
            help_text=_('auto|length|cover|contain|initial|inherit'))

    additional_class_names = models.TextField(
        verbose_name=_('additional classes'),
        blank=True,
        help_text=_('Comma separated list of additional classes to apply to '
                    'tag_type')
    )

    def __str__(self):
        display = self.tag_type or ''
        if self.additional_class_names:
            display = '{0} ({1})'.format(display, self.additional_class_names)
        if self.label:
            display = '“{0}”: {1}'.format(self.label, display)
        return display

    def clean(self):
        if self.additional_class_names:
            additional_class_names = list(
                html_class.strip() for html_class in
                self.additional_class_names.split(','))
            for class_name in additional_class_names:
                class_name = class_name.strip()
                if not CLASS_NAME_FORMAT.match(class_name):
                    raise ValidationError(
                        _('"{0}" is not a proper css class name.').format(
                            class_name)
                    )
            self.additional_class_names = ', '.join(
                set(additional_class_names))

    @property
    def get_additional_class_names(self):
        if self.additional_class_names:
            # Removes any extra spaces
            return ' '.join((
                html_class.strip() for html_class in
                self.additional_class_names.split(',')))
        return ''

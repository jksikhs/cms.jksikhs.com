# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):
    enable_rest_framework = forms.CheckboxField(
        'Enable Django REST Framework',
        required=False,
        initial=True,
    )

    permissions_policy = forms.CharField(
        'Django REST Framework Permissions Policy',
        required=False,
        initial='AllowAny',
        help_text=(
            'REST Framework Permissions Policies are described at '
            'http://www.django-rest-framework.org/api-guide/permissions/ '
        )
    )

    def to_settings(self, data, settings):
        enable_rest_framework = data['enable_rest_framework']
        permissions_policy = (
            'rest_framework.permissions.{}'.format(
                data['permissions_policy']
            )
        )

        if enable_rest_framework:
            settings['INSTALLED_APPS'].extend([
                'rest_framework',
            ])
            settings['ADDON_URLS'].append('aldryn_django_rest_framework.urls')
            settings['REST_FRAMEWORK'] = {
                'DEFAULT_PERMISSION_CLASSES': (permissions_policy,)
            }
        return settings

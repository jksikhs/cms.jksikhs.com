"""
Configuration for Divio cloud.

We don't allow configuration via the Control Panel, hence
there's not much to do here. For the docs see:
https://docs.divio.com/en/latest/reference/configuration-aldryn-config.html
"""
from aldryn_client import forms


class Form(forms.BaseForm):
    """Divio Control Panel configuration form"""

    def to_settings(self, data, settings):
        return settings

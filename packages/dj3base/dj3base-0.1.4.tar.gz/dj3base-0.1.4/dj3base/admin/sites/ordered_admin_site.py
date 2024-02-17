# -*- coding: utf-8 -*-
from django.contrib.admin.sites import AdminSite


_DEFAULT_INDEX = 99999


class OrderedAdminSite(AdminSite):
    ordered_apps = dict()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ordered_apps = dict()
        for app_config, info in self.ordered_apps.items():
            app_label = app_config.name.split('.')[-1]
            self._ordered_apps[app_label] = info

    def get_app_list(self, request, app_label=None):
        app_dict = self._build_app_dict(request, app_label)
        for label, app_info in app_dict.items():
            app_index_info = self._ordered_apps.get(label, None)
            if app_index_info is not None:
                app_info['index'] = app_index_info['index']
                for model_info in app_info['models']:
                    model_index_info = app_index_info['models'].get(model_info['model'], None)
                    if model_index_info is not None:
                        model_info['index'] = model_index_info['index']

        app_list = sorted(app_dict.values(), key=lambda x: x.get("index", _DEFAULT_INDEX))

        for app in app_list:
            app["models"].sort(key=lambda x: x.get("index", _DEFAULT_INDEX))

        return app_list

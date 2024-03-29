#encoding:utf-8
"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'doc_django.menu.CustomMenu'
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    """
    Custom Menu for doc_django admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(u"MAGAZINE.ORG", reverse('admin:index')),
            items.Bookmarks(),
            items.AppList(
                    u"Меню управлением сайта",
                exclude=('django.contrib.*',)
            ),
            items.AppList(
                u"Администрирование",
                models=('django.contrib.*',)
            ),
            items.MenuItem('Multi level menu item',
                           children=[
                               items.MenuItem('Blog', '/admin/app/blog/'),
                               items.MenuItem('Child 2', '/bar/'),
                               ])

        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)

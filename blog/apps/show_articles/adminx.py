import xadmin
from xadmin import views
from .models import Articles


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "个人博客后台系统"
    site_footer = "个人博客后台系统"
    menu_style = "accordion"


class ArticlesAdmin(object):
    list_filter = ['article_id', 'article_name', 'article_desc', 'add_time']
    list_display = ['article_id', 'article_name', 'article_desc', 'add_time']
    search_fields = ['article_id', 'article_name', 'article_desc', 'add_time']


xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

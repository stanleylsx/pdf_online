from django.shortcuts import render
from django.views.generic.base import View
from .models import Articles


# Create your views here.

class ArticlesView(View):
    """
    文章展示
    """

    @staticmethod
    def get(request, article_id):
        para_dict = {}
        article_item = Articles.objects.filter(article_id=article_id)[0]
        para_dict['article_item'] = article_item
        return render(request, 'show_article.html', para_dict)


# 全局404处理函数
def pageNotFound(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# 全局500处理函数
def pageError(request):
    from django.shortcuts import render_to_response
    response = render_to_response("500.html", {})
    response.status_code = 500
    return response

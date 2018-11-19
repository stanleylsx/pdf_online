from django.db import models
from datetime import datetime


# Create your models here.
class Articles(models.Model):
    """
    存放自己的文章的model
    """
    article_id = models.AutoField(primary_key=True)
    article_name = models.CharField(max_length=50, verbose_name="文章的名字")
    article_desc = models.CharField(max_length=300, verbose_name="文章的描述")
    pdf_url = models.FileField(upload_to="pdf/%Y/%m/%d/", null=True, blank=True, verbose_name="PDF格式的文章")
    page_icon = models.ImageField(upload_to="icon/pdf/%Y/%m/%d/", verbose_name="pdf页面的icon", max_length=100, default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="文件上传时间")

    class Meta:
        verbose_name = "我的文章"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.article_name

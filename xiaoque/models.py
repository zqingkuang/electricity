from django.db import models
from blemish.models import BlemishTask
from user.models import User


class BehebungTack(models.Model):
    """消缺任务模型类"""
    ORDER_STATUS_CHOICES = (
        (0, '执行中'),
        (1, '已完成')

    )
    b_number = models.CharField(max_length=10, verbose_name='任务编号')
    b_blemish = models.ForeignKey(BlemishTask, on_delete=models.CASCADE, verbose_name='缺陷任务')
    b_name = models.CharField(max_length=10, verbose_name='消缺任务名称')
    b_voucher = models.CharField(max_length=50, verbose_name='工作单据')
    b_user = models.CharField(max_length=10, verbose_name='负责人')
    b_issuer = models.CharField(max_length=10, verbose_name='发布人')
    b_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    b_describe = models.CharField(max_length=200, verbose_name='任务描述')
    b_remarks = models.CharField(max_length=200, verbose_name='备注')
    b_state = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='消缺任务状态')
    b_completion_time = models.DateTimeField(default=None, verbose_name='消缺任务完成时间')
    b_staff = models.ManyToManyField(User, verbose_name='消缺员')

    def status(self):
        if self.b_state == 0:
            return '执行中'
        else:
            return '已完成'




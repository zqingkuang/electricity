from django.db import models

from pole.models import Pole
from user.models import User


class Blemish(models.Model):
    """缺陷模型类"""
    ORDER_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用'),
    )
    b_name = models.CharField(max_length=10, verbose_name='缺陷名称')
    b_state = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='缺陷状态')

    def status(self):
        if self.b_state == 0:
            return '启用'
        else:
            return '禁用'


class BlemishTask(models.Model):
    """缺陷任务模型类"""
    b_pole = models.ForeignKey(Pole, on_delete=models.CASCADE, verbose_name='塔杆对应外键')
    b_blemish = models.ForeignKey(Blemish, on_delete=models.CASCADE, verbose_name='缺陷类型')
    b_rank = models.CharField(max_length=10, verbose_name='缺陷级别')
    b_rate = models.CharField(max_length=10, verbose_name='完好率')
    b_time = models.DateTimeField(auto_now_add=True, verbose_name='发现时间')
    b_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='发现人')
    b_describe = models.CharField(max_length=300, verbose_name='缺陷描述')
    b_affirm_user = models.CharField(max_length=10, null=True, verbose_name='确认人')


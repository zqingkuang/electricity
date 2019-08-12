from django.db import models
from pole.models import Circuit
from user.models import User
from blemish.models import BlemishTask


class Inspection(models.Model):
    """巡检任务模型类"""
    ORDER_STATUS_CHOICES = (
        (0, '待分配'),
        (1, '已分配'),
        (2, '执行中'),
        (3, '已完成')
    )
    i_number = models.CharField(max_length=10, verbose_name='任务编号')
    i_name = models.CharField(max_length=20, verbose_name='任务名称')
    i_circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE, verbose_name='任务线路')
    i_user = models.ManyToManyField(User, verbose_name='巡检人员')
    issuer = models.CharField(max_length=10, verbose_name='任务发布人')
    i_time = models.DateTimeField(auto_now_add=True, verbose_name='任务发布时间')
    i_remark = models.CharField(max_length=200, verbose_name='任务备注', null=True)
    i_state = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='任务状态')
    i_finish_time = models.DateTimeField(default=None, verbose_name='任务完成时间')
    i_blemish = models.ForeignKey(BlemishTask, on_delete=models.CASCADE, null=True, verbose_name='缺陷类型')

    def stats(self):
        if self.i_state == 0:
            return '待分配'
        elif self.i_state == 2:
            return '执行中'
        elif self.i_state == 3:
            return '已完成'
        else:
            return '已分配'



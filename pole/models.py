from django.db import models


class Circuit(models.Model):
    """线路模型类"""
    ORDER_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用'),
        (2, '检修中')
    )
    c_number = models.CharField(max_length=10, verbose_name='线路编号')
    c_name = models.CharField(max_length=10, verbose_name='线路名称')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='线路创建时间')
    c_voltage = models.IntegerField(verbose_name='电压等级')
    c_remark = models.CharField(max_length=200, verbose_name='线路备注', null=True)
    c_state = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='线路状态')

    def stats(self):
        if self.c_state == 0:
            return '启用'
        elif self.c_state == 2:
            return '检修中'
        else:
            return '禁用'


class Pole(models.Model):
    """塔杆模型类"""
    ORDER_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用'),
        (2, '检修中')
    )
    p_number = models.CharField(max_length=10, verbose_name='塔杆编号')
    p_circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE, verbose_name='塔杆所属线路')
    p_state = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='塔杆状态')
    p_remark = models.CharField(max_length=200, verbose_name='塔杆备注', null=True)

    def stats(self):
        if self.p_state == 0:
            return '启用'
        elif self.p_state == 2:
            return '检修中'
        else:
            return '禁用'


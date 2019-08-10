from django.db import models


class Role(models.Model):
    """角色模型类"""
    ORDER_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用')
    )
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name='角色创建时间')
    r_name = models.CharField(max_length=10, verbose_name='角色名称')
    change_time = models.DateTimeField(auto_now=True, verbose_name='角色')
    r_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='状态')

    def status(self):
        if self.r_status == 0:
            return '启用'
        else:
            return '禁用'


class Jurisdiction(models.Model):
    """权限模型类"""
    j_name = models.CharField(max_length=30, verbose_name='权限名称')
    j_jurisdiction = models.ManyToManyField(Role)


class User(models.Model):
    """用户模型类"""
    ORDER_STATUS_SEX = (
        (0, '男'),
        (1, '女')
    )
    ORDER_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用')
    )
    user = models.CharField(max_length=10, verbose_name='用户账号')
    password = models.CharField(max_length=15, verbose_name='用户密码')
    name = models.CharField(max_length=10, verbose_name='用户姓名')
    email = models.EmailField(verbose_name='用户邮箱', null=True)
    age = models.IntegerField(verbose_name='用户年龄', null=True)
    u_sex = models.SmallIntegerField(choices=ORDER_STATUS_SEX, verbose_name='用户性别', null=True)
    phone = models.CharField(max_length=11, verbose_name='用户电话', null=True)
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name='入职时间')
    address = models.CharField(max_length=50, verbose_name='用户地址', null=True)
    change_time = models.DateTimeField(auto_now=True, verbose_name='用户上次修改时间')
    u_state = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='用户状态')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='用户角色')
    # group = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True, verbose_name='用户所属组')
    u_resignation_time = models.DateTimeField(default=None, verbose_name='离职时间')

    def sex(self):
        if self.u_sex == 0:
            return '男'
        else:
            return '女'

    def states(self):
        if self.u_state == 0:
            return '启用'
        else:
            return '禁用'



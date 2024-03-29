# Generated by Django 2.1.3 on 2019-08-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j_name', models.CharField(max_length=30, verbose_name='权限名称')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True, verbose_name='角色创建时间')),
                ('r_name', models.CharField(max_length=10, verbose_name='角色名称')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='角色')),
                ('r_status', models.SmallIntegerField(choices=[(0, '启用'), (1, '禁用')], verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10, verbose_name='用户账号')),
                ('password', models.CharField(max_length=15, verbose_name='用户密码')),
                ('name', models.CharField(max_length=10, verbose_name='用户姓名')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='用户邮箱')),
                ('age', models.IntegerField(null=True, verbose_name='用户年龄')),
                ('u_sex', models.SmallIntegerField(choices=[(0, '男'), (1, '女')], null=True, verbose_name='用户性别')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='用户电话')),
                ('entry_time', models.DateTimeField(auto_now_add=True, verbose_name='入职时间')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='用户地址')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='用户上次修改时间')),
                ('u_state', models.SmallIntegerField(choices=[(0, '启用'), (1, '禁用')], verbose_name='用户状态')),
                ('u_resignation_time', models.DateTimeField(default=None, verbose_name='离职时间')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Role', verbose_name='用户角色')),
            ],
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='j_jurisdiction',
            field=models.ManyToManyField(to='user.Role'),
        ),
    ]

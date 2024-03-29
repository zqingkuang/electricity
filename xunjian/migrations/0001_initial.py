# Generated by Django 2.1.3 on 2019-08-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pole', '0001_initial'),
        ('blemish', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_number', models.CharField(max_length=10, verbose_name='任务编号')),
                ('i_name', models.CharField(max_length=20, verbose_name='任务名称')),
                ('issuer', models.CharField(max_length=10, verbose_name='任务发布人')),
                ('i_time', models.DateTimeField(auto_now_add=True, verbose_name='任务发布时间')),
                ('i_remark', models.CharField(max_length=200, null=True, verbose_name='任务备注')),
                ('i_state', models.SmallIntegerField(choices=[(0, '待分配'), (1, '已分配'), (2, '执行中'), (3, '已完成')], verbose_name='任务状态')),
                ('i_finish_time', models.DateTimeField(default=None, verbose_name='任务完成时间')),
                ('i_blemish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blemish.Blemish', verbose_name='缺陷类型')),
                ('i_circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pole.Circuit', verbose_name='任务线路')),
                ('i_user', models.ManyToManyField(to='user.User', verbose_name='巡检人员')),
            ],
        ),
    ]

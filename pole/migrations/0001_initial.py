# Generated by Django 2.1.3 on 2019-08-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_number', models.CharField(max_length=10, verbose_name='线路编号')),
                ('c_name', models.CharField(max_length=10, verbose_name='线路名称')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='线路创建时间')),
                ('c_voltage', models.IntegerField(verbose_name='电压等级')),
                ('c_remark', models.CharField(max_length=200, null=True, verbose_name='线路备注')),
                ('c_state', models.SmallIntegerField(choices=[(0, '启用'), (1, '禁用'), (2, '检修中')], verbose_name='线路状态')),
            ],
        ),
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_number', models.CharField(max_length=10, verbose_name='塔杆编号')),
                ('p_state', models.SmallIntegerField(choices=[(0, '启用'), (1, '禁用'), (2, '检修中')], verbose_name='塔杆状态')),
                ('p_remark', models.CharField(max_length=200, null=True, verbose_name='塔杆备注')),
                ('p_circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pole.Circuit', verbose_name='塔杆所属线路')),
            ],
        ),
    ]

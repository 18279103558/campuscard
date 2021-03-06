# Generated by Django 2.0.5 on 2018-05-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rechargerecord_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.FloatField(verbose_name='余额'),
        ),
        migrations.AlterField(
            model_name='card',
            name='state',
            field=models.CharField(choices=[('valid', '有效'), ('invalid', '无效')], max_length=10, verbose_name='状态'),
        ),
    ]

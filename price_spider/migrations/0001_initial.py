# Generated by Django 2.1.5 on 2019-01-29 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='商品类型')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='商品名称')),
            ],
        ),
        migrations.CreateModel(
            name='LatestRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='最新数据日期')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='数据日期')),
                ('price', models.FloatField(verbose_name='均价')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_spider.Category', verbose_name='商品类型')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_spider.Goods', verbose_name='商品')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='单位')),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_spider.Unit', verbose_name='单位'),
        ),
    ]

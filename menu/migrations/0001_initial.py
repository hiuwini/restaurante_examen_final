# Generated by Django 2.2.7 on 2019-11-21 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Plato')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='platos',
            field=models.ManyToManyField(through='menu.Venta', to='menu.Plato'),
        ),
    ]

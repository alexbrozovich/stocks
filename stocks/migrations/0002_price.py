# Generated by Django 2.1 on 2018-08-14 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar_value', models.CharField(max_length=10)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock')),
            ],
        ),
    ]

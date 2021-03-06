# Generated by Django 3.2.7 on 2021-10-16 14:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orders_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date_purchase',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=254)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('register_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.register')),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.productcomment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='ManageAddress',
            fields=[
                ('manageAddId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=254)),
                ('fullName', models.CharField(default='', max_length=100)),
                ('fullAddress', models.CharField(default='', max_length=300)),
                ('phone', models.CharField(default='', max_length=10)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip_code', models.CharField(default='', max_length=50)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
        ),
    ]

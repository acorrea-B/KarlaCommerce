# Generated by Django 3.2.5 on 2021-07-31 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchases', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Transaction')),
                ('value', models.IntegerField()),
                ('state', models.CharField(max_length=200)),
                ('token', models.CharField(blank=True, max_length=250)),
                ('creation_date', models.DateField()),
                ('close_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True)),
                ('client_ip', models.CharField(max_length=25)),
                ('operator', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('purchase', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchases.purchasemodel', verbose_name='Purchases')),
            ],
        ),
    ]

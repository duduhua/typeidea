# Generated by Django 2.2.5 on 2019-10-17 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20191017_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]

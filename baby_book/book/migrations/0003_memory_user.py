# Generated by Django 3.1.3 on 2020-12-06 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0002_auto_20201206_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='user',
            field=models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]

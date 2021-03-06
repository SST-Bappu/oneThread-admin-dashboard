# Generated by Django 3.1.7 on 2022-01-20 08:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issueType', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('issueDetails', models.CharField(max_length=500)),
                ('imageUrl', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

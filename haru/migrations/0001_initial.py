# Generated by Django 5.0.3 on 2024-05-08 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DIARY_DETAIl',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('SHORT_TEXT', models.TextField()),
                ('FEEDBACK_TEXT', models.TextField()),
                ('FEEDBACK_FILE_DIR', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Haru_setting',
            fields=[
                ('USER_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('HARU_OLD', models.IntegerField()),
                ('HARU_STYLE', models.IntegerField()),
                ('HARU_GENDER', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DIARY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATE', models.DateTimeField(blank=True, null=True)),
                ('EMO', models.CharField(max_length=30)),
                ('ORI_FILE_DIR', models.TextField()),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

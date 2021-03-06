# Generated by Django 3.0.5 on 2020-10-10 10:49

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
            name='Hospital',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Street', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Pincode', models.CharField(max_length=6)),
                ('Phone_No', models.CharField(max_length=14)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_hospital', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

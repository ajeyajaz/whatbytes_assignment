# Generated by Django 5.2.3 on 2025-06-22 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0002_alter_doctor_specialization'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'unique_together': {('patient', 'doctor')},
            },
        ),
    ]

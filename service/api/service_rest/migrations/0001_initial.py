# Generated by Django 4.0.3 on 2022-08-01 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobileVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VIN', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('employee_number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VIN', models.BigIntegerField()),
                ('owner', models.CharField(max_length=30)),
                ('date_time', models.DateTimeField()),
                ('reason', models.TextField()),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='technician', to='service_rest.technician')),
            ],
        ),
    ]
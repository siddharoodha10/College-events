# Generated by Django 3.2.6 on 2021-09-12 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_id', models.CharField(max_length=100)),
                ('E_name', models.CharField(max_length=100)),
                ('E_type', models.CharField(choices=[('cultural', 'Cultural'), ('technical', 'Technical')], default='Cultural', max_length=100)),
                ('E_location', models.CharField(max_length=100)),
                ('E_date', models.DateField(default=2000)),
                ('E_time', models.TimeField()),
                ('E_fees', models.IntegerField(default=30)),
                ('E_coordinator_no', models.CharField(max_length=100)),
                ('E_image', models.ImageField(default='static/image1.jpg', upload_to='pics')),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=30)),
                ('sem', models.IntegerField()),
                ('college', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(default=0, max_length=100)),
                ('Even_fees', models.IntegerField(default=30)),
                ('payment_mode', models.CharField(default=0, max_length=100)),
                ('account_no', models.CharField(default=0, max_length=100)),
                ('cvv', models.IntegerField(default=0)),
                ('exp_date', models.DateField(default=2008)),
                ('E_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='event.event')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]

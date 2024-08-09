# Generated by Django 5.0.7 on 2024-08-08 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('closed_won', 'Closed Won'), ('closed_lost', 'Closed Lost')], default='new', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]

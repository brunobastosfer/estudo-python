# Generated by Django 5.0.1 on 2024-01-15 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_alter_todo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=9),
        ),
    ]

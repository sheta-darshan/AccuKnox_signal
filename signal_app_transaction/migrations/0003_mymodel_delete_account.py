# Generated by Django 5.1.1 on 2024-09-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signal_app_transaction', '0002_remove_account_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]

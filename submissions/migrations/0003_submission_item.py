# Generated by Django 2.2.11 on 2020-07-14 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plaidapp', '0001_initial'),
        ('submissions', '0002_submission_monthly_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='item',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='plaidapp.PlaidItem'),
        ),
    ]

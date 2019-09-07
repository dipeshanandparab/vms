# Generated by Django 2.2.4 on 2019-09-01 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=20)),
                ('purpose', models.CharField(max_length=200)),
                ('visit_date', models.DateTimeField(verbose_name='visit_date')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.Company')),
            ],
        ),
    ]

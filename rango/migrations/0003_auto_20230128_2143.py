# Generated by Django 2.1.7 on 2023-01-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_alter_category_id_alter_page_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
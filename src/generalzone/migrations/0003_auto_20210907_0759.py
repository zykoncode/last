# Generated by Django 3.2.7 on 2021-09-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0002_career_complain_logininfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='logininfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
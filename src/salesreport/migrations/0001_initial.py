# Generated by Django 3.2.4 on 2021-06-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=150)),
                ('Contact_Person', models.CharField(max_length=150)),
                ('Designation', models.CharField(max_length=50)),
                ('Mobile_num', models.IntegerField()),
                ('Login_person', models.CharField(max_length=50)),
                ('Existing_Customer', models.BooleanField(default='True')),
            ],
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-02 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsLib', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='borrow_time',
            new_name='borrowed_time',
        ),
    ]

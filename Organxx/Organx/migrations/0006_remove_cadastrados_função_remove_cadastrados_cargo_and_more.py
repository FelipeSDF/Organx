# Generated by Django 5.1 on 2024-08-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organx', '0005_alter_cadastrados_função_alter_cadastrados_cargo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastrados',
            name='Função',
        ),
        migrations.RemoveField(
            model_name='cadastrados',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='cadastrados',
            name='email',
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]

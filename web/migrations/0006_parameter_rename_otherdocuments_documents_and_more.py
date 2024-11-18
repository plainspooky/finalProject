# Generated by Django 4.2 on 2024-10-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(help_text='Norma, Lei, Resolução', max_length=200, verbose_name='standard')),
                ('description', models.CharField(help_text='Parâmetro', max_length=200, verbose_name='parametro')),
                ('type', models.CharField(help_text='Tipos de Parâmetros(físico-químicos, microbiologicos)', max_length=80, verbose_name='tipos')),
            ],
        ),
        migrations.RenameModel(
            old_name='OtherDocuments',
            new_name='Documents',
        ),
        migrations.RenameField(
            model_name='environmentalconsultancy',
            old_name='other_documents',
            new_name='documents',
        ),
    ]
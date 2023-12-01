# Generated by Django 4.2.4 on 2023-11-15 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdffile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='files')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Excelfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(upload_to='files')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Docfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='files')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userdetail')),
            ],
        ),
    ]

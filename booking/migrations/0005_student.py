# Generated by Django 4.1.1 on 2022-09-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_subject_academic_year_remove_subject_quota_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('subjects', models.ManyToManyField(blank=True, related_name='Students', to='booking.register')),
            ],
        ),
    ]
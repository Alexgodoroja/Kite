# Generated by Django 4.1.3 on 2023-03-22 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_featuredbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.featuredbook'),
        ),
    ]

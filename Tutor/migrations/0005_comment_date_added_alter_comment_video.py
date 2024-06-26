# Generated by Django 4.1.5 on 2023-02-01 07:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Tutor.video'),
        ),
    ]

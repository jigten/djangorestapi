# Generated by Django 3.0.8 on 2020-07-04 13:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

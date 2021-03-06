# Generated by Django 3.1.7 on 2021-04-08 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='Event',
            new_name='Note',
        ),
        migrations.DeleteModel(
            name='EventMember',
        ),
        migrations.AddField(
            model_name='notemember',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.note'),
        ),
        migrations.AddField(
            model_name='notemember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='notemember',
            unique_together={('note', 'user')},
        ),
    ]

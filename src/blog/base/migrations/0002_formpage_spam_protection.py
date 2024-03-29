# Generated by Django 2.2.4 on 2019-08-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='spam_protection',
            field=models.BooleanField(default=True, help_text='When enabled, the CMS will filter out spam form submissions for this page.', verbose_name='Spam Protection'),
        ),
    ]

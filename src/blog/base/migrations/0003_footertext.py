# Generated by Django 2.2.4 on 2019-08-28 20:53

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_formpage_spam_protection'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Footer Text',
            },
        ),
    ]
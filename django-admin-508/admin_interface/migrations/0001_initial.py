# Generated by Django 3.2.3 on 2021-07-01 17:57

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Django', max_length=50, unique=True, verbose_name='name')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('title', models.CharField(blank=True, default='Django administration', max_length=50, verbose_name='title')),
                ('title_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='color')),
                ('title_visible', models.BooleanField(default=True, verbose_name='visible')),
                ('logo', models.FileField(blank=True, help_text='Leave blank to use the default Django logo', upload_to='admin-interface/logo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'jpg', 'jpeg', 'png', 'svg'])], verbose_name='logo')),
                ('logo_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='color')),
                ('logo_visible', models.BooleanField(default=True, verbose_name='visible')),
                ('favicon', models.FileField(blank=True, help_text='(.ico|.png|.gif - 16x16|32x32 px)', upload_to='admin-interface/favicon/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'ico', 'jpg', 'jpeg', 'png', 'svg'])], verbose_name='favicon')),
                ('env_name', models.CharField(blank=True, max_length=50, verbose_name='name')),
                ('env_color', colorfield.fields.ColorField(blank=True, default='#E74C3C', help_text='(red: #E74C3C, orange: #E67E22, yellow: #F1C40F, green: #2ECC71, blue: #3498DB)', max_length=10, verbose_name='color')),
                ('env_visible_in_header', models.BooleanField(default=True, verbose_name='visible in header (marker and name)')),
                ('env_visible_in_favicon', models.BooleanField(default=True, verbose_name='visible in favicon (marker)')),
                ('language_chooser_active', models.BooleanField(default=True, verbose_name='active')),
                ('language_chooser_display', models.CharField(choices=[('code', 'code'), ('name', 'name')], default='code', max_length=10, verbose_name='display')),
                ('css_header_background_color', colorfield.fields.ColorField(blank=True, default='#112E51', help_text='#112E51', max_length=10, verbose_name='background color')),
                ('css_header_text_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='text color')),
                ('css_header_link_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='link color')),
                ('css_header_link_hover_color', colorfield.fields.ColorField(blank=True, default='#E1F3F8', help_text='#E1F3F8', max_length=10, verbose_name='link hover color')),
                ('css_module_background_color', colorfield.fields.ColorField(blank=True, default='#205493', help_text='#205493', max_length=10, verbose_name='background color')),
                ('css_module_background_selected_color', colorfield.fields.ColorField(blank=True, default='#FFFFCC', help_text='#FFFFCC', max_length=10, verbose_name='background selected color')),
                ('css_module_text_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='text color')),
                ('css_module_link_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='link color')),
                ('css_module_link_selected_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='link selected color')),
                ('css_module_link_hover_color', colorfield.fields.ColorField(blank=True, default='#E1F3F8', help_text='#E1F3F8', max_length=10, verbose_name='link hover color')),
                ('css_module_rounded_corners', models.BooleanField(default=True, verbose_name='rounded corners')),
                ('css_generic_link_color', colorfield.fields.ColorField(blank=True, default='#205493', help_text='#205493', max_length=10, verbose_name='link color')),
                ('css_generic_link_hover_color', colorfield.fields.ColorField(blank=True, default='#0071BC', help_text='#0071BC', max_length=10, verbose_name='link hover color')),
                ('css_save_button_background_color', colorfield.fields.ColorField(blank=True, default='#205493', help_text='#205493', max_length=10, verbose_name='background color')),
                ('css_save_button_background_hover_color', colorfield.fields.ColorField(blank=True, default='#112E51', help_text='#112E51', max_length=10, verbose_name='background hover color')),
                ('css_save_button_text_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='text color')),
                ('css_delete_button_background_color', colorfield.fields.ColorField(blank=True, default='#CD2026', help_text='#CD2026', max_length=10, verbose_name='background color')),
                ('css_delete_button_background_hover_color', colorfield.fields.ColorField(blank=True, default='#981B1E', help_text='#981B1E', max_length=10, verbose_name='background hover color')),
                ('css_delete_button_text_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='text color')),
                ('css', models.TextField(blank=True, verbose_name='text color')),
                ('related_modal_active', models.BooleanField(default=True, verbose_name='active')),
                ('related_modal_background_color', colorfield.fields.ColorField(blank=True, default='#000000', help_text='#000000', max_length=10, verbose_name='background color')),
                ('related_modal_background_opacity', models.CharField(choices=[('0.1', '10%'), ('0.2', '20%'), ('0.3', '30%'), ('0.4', '40%'), ('0.5', '50%'), ('0.6', '60%'), ('0.7', '70%'), ('0.8', '80%'), ('0.9', '90%')], default='0.8', help_text='80%', max_length=5, verbose_name='background opacity')),
                ('related_modal_rounded_corners', models.BooleanField(default=True, verbose_name='rounded corners')),
                ('related_modal_close_button_visible', models.BooleanField(default=True, verbose_name='close button visible')),
                ('list_filter_dropdown', models.BooleanField(default=True, verbose_name='use dropdown')),
                ('list_filter_sticky', models.BooleanField(default=True, verbose_name='sticky position')),
                ('recent_actions_visible', models.BooleanField(default=True, verbose_name='visible')),
                ('form_submit_sticky', models.BooleanField(default=False, verbose_name='sticky submit')),
                ('form_pagination_sticky', models.BooleanField(default=False, verbose_name='sticky pagination')),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
    ]
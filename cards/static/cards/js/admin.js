/**
 * Created by JOph on 2019/1/13.
 */

var react = function () {
        if (django.jQuery('#id_special').val() == 'ruse') {
            django.jQuery('#id_Inlines[0]').parent().parent().show(500);
            django.jQuery('#id_image').parent().parent().hide(500);
            django.jQuery('#id_cropping').parent().parent().hide(500);
        }
        else {
            if (django.jQuery('#id_special').val() == 'power') {
                django.jQuery('#id_content').parent().parent().hide(500);
                django.jQuery('#id_image').parent().parent().show(500);
                django.jQuery('#id_cropping').parent().parent().show(500);
            }
        }
        };

        django.jQuery(function () {
            react();
            django.jQuery('#id_special').on('change', react);
        });
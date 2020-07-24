from django.contrib import admin

from adbpo_geonode.themes.models import (ADBPOCustomGeonodeTheme,
                                         ADBPOJumbotronSlideShow)
from geonode.themes.admin import (GeonodeThemCustomizationForm,
                                  GeoNodeThemeCustomizationAdmin)
from geonode.themes.models import GeoNodeThemeCustomization


class ADBPOCustomGeonodeThemeAdmin(GeoNodeThemeCustomizationAdmin):
    form = GeonodeThemCustomizationForm
    exclude = ['jumbotron_welcome_content', 'jumbotron_bg']

    fields = ['name', 'description', 'is_enabled', 'logo', 'jumbotron_welcome_hide', 'jumbotron_welcome_title', 'jumbotron_slide_show', 'partners', 'jumbotron_cta_hide', 'jumbotron_cta_text', 'jumbotron_cta_link', 'body_color', 'body_text_color', 'navbar_color', 'navbar_text_color', 'navbar_text_hover', 'navbar_text_hover_focus', 'navbar_dropdown_menu', 'navbar_dropdown_menu_text', 'navbar_dropdown_menu_hover', 'navbar_dropdown_menu_divider', 'jumbotron_color', 'jumbotron_title_color', 'jumbotron_text_color', 'search_bg_color', 'search_title_color', 'search_link_color', 'contactus', 'contact_name', 'contact_position', 'contact_administrative_area', 'contact_street', 'contact_postal_code', 'contact_city', 'contact_country', 'contact_delivery_point', 'contact_voice', 'contact_facsimile', 'contact_email', 'partners_title', 'copyright', 'copyright_color', 'footer_bg_color', 'footer_text_color', 'footer_href_color', 'cookie_law_info_bar_enabled', 'cookie_law_info_bar_head', 'cookie_law_info_bar_text', 'cookie_law_info_leave_url', 'cookie_law_info_showagain_head', 'cookie_law_info_data_controller', 'cookie_law_info_data_controller_address', 'cookie_law_info_data_controller_phone', 'cookie_law_info_data_controller_email', 'cookie_law_info_animate_speed_hide', 'cookie_law_info_animate_speed_show', 'cookie_law_info_background', 'cookie_law_info_border', 'cookie_law_info_border_on', 'cookie_law_info_button_1_button_colour', 'cookie_law_info_button_1_button_hover', 'cookie_law_info_button_1_link_colour', 'cookie_law_info_button_1_as_button',
              'cookie_law_info_button_1_new_win', 'cookie_law_info_button_2_button_colour', 'cookie_law_info_button_2_button_hover', 'cookie_law_info_button_2_link_colour', 'cookie_law_info_button_2_as_button', 'cookie_law_info_button_2_hidebar', 'cookie_law_info_button_3_button_colour', 'cookie_law_info_button_3_button_hover', 'cookie_law_info_button_3_link_colour', 'cookie_law_info_button_3_as_button', 'cookie_law_info_button_3_new_win', 'cookie_law_info_button_4_button_colour', 'cookie_law_info_button_4_button_hover', 'cookie_law_info_button_4_link_colour', 'cookie_law_info_button_4_as_button', 'cookie_law_info_font_family', 'cookie_law_info_header_fix', 'cookie_law_info_notify_animate_hide', 'cookie_law_info_notify_animate_show', 'cookie_law_info_notify_div_id', 'cookie_law_info_notify_position_horizontal', 'cookie_law_info_notify_position_vertical', 'cookie_law_info_scroll_close', 'cookie_law_info_scroll_close_reload', 'cookie_law_info_accept_close_reload', 'cookie_law_info_reject_close_reload', 'cookie_law_info_showagain_tab', 'cookie_law_info_showagain_background', 'cookie_law_info_showagain_border', 'cookie_law_info_showagain_div_id', 'cookie_law_info_showagain_x_position', 'cookie_law_info_text', 'cookie_law_info_show_once_yn', 'cookie_law_info_show_once', 'cookie_law_info_logging_on', 'cookie_law_info_as_popup', 'cookie_law_info_popup_overlay', 'cookie_law_info_bar_heading_text', 'cookie_law_info_cookie_bar_as', 'cookie_law_info_popup_showagain_position', 'cookie_law_info_widget_position']


class ADBPOJumbotronSlideShowAdmin(admin.ModelAdmin):
    pass


admin.site.register(ADBPOCustomGeonodeTheme, ADBPOCustomGeonodeThemeAdmin)
admin.site.register(ADBPOJumbotronSlideShow, ADBPOJumbotronSlideShowAdmin)
admin.site.unregister(GeoNodeThemeCustomization)

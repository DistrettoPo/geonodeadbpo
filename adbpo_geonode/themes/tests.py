from adbpo_geonode.themes.context_processors import custom_theme
from adbpo_geonode.themes.models import (ADBPOCustomGeonodeTheme,
                                         ADBPOJumbotronSlideShow)
from geonode.tests.base import GeoNodeBaseTestSupport


class TestADBPOCustomTheme(GeoNodeBaseTestSupport):
    def setUp(self):
        super(TestADBPOCustomTheme, self).setUp()

    def test_context_with_empty_theme(self):
        theme_context = custom_theme(None)
        self.assertEqual(
            theme_context, {'custom_theme': {}, 'slide_count': 0, 'slideshow': []})

    def test_context_with_theme(self):
        slide_show = ADBPOJumbotronSlideShow.objects.create(
            slide_name='test-slide')
        theme = ADBPOCustomGeonodeTheme.objects.create(
            name='test-theme', is_enabled=True)
        theme.jumbotron_slide_show.add(slide_show)
        theme_context = custom_theme(None)
        self.assertEqual(theme_context, {
            'custom_theme': theme,
            'slide_count': 1,
            'slideshow': [{
                'index': 0,
                'slide': slide_show
            }]
        })

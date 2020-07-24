
from django.core.cache import cache

from adbpo_geonode.themes.models import ADBPOCustomGeonodeTheme
from geonode.themes.models import THEME_CACHE_KEY


def custom_theme(request):
    theme = cache.get(THEME_CACHE_KEY)
    if theme is None:
        try:
            theme = ADBPOCustomGeonodeTheme.objects.prefetch_related(
                'partners').get(is_enabled=True)
            slides = theme.jumbotron_slide_show.filter(is_enabled=True)
            slideshow = [{'slide': slide, 'index': ind} for ind,
                         slide in enumerate(slides)]
        except Exception as e:
            theme = {}
            slideshow = []
            slides = 0
        cache.set(THEME_CACHE_KEY, theme)
    return {
        'custom_theme': theme,
        'slideshow': slideshow,
        'slide_count': slides.count() if slides else slides
    }

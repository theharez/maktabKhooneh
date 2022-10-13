from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['website:home_view', 'website:about_view', 'website:contact_view']

    def location(self, item):
        return reverse(item)
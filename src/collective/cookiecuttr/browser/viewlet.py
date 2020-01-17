# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from collective.cookiecuttr.interfaces import ICookieCuttrSettings
from plone.app.layout.analytics.view import AnalyticsViewlet
from plone.memoize.view import memoize
from plone.registry.interfaces import IRegistry
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.interface import implementer
from zope.viewlet.interfaces import IViewlet

@implementer(IViewlet)
class CookieCuttrViewlet(BrowserView):

    def __init__(self, context, request, view, manager):
        super(CookieCuttrViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.settings = getUtility(IRegistry).forInterface(
            ICookieCuttrSettings,
            check=False,
        )

    def update(self):
        pass

    @memoize
    def language(self):
        pps = getMultiAdapter(
            (self.context, self.request),
            name=u'plone_portal_state'
        )
        return pps.language()

    @memoize
    def values_to_dict(self):
        link = self.settings.link
        text = self.settings.text
        accept = self.settings.accept_button
        data = {}
        if link and text and accept:
            for item in link:
                dic = data.get(item.get('language'), {})
                dic['link'] = item.get('text')
                data[item.get('language')] = dic

            for item in text:
                dic = data.get(item.get('language'), {})
                dic['text'] = item.get('text')
                data[item.get('language')] = dic

            for item in accept:
                dic = data.get(item.get('language'), {})
                dic['accept'] = item.get('text')
                data[item.get('language')] = dic

            data['_default_'] = dict(
                link=link[0].get('text'),
                text=text[0].get('text'),
                accept=accept[0].get('text'),
            )
        return data

    def available(self):
        return self.settings and self.settings.cookiecuttr_enabled

    def render(self):
        if self.available():
            dic = self.values_to_dict()
            if dic:
                default = dic.get('_default_')
                link = dic.get(self.language(), default).get('link')
                text = dic.get(self.language(), default).get('text')
                accept_button = dic.get(self.language(), default).get('accept')
                location_bottom = 'false'
                if self.settings.location_bottom:
                    location_bottom = 'true'
                snippet = safe_unicode(js_template % (link,
                                                      text,
                                                      accept_button,
                                                      location_bottom))
                return snippet
            else:
                from logging import getLogger
                log = getLogger(__name__)
                log.debug('There are no available messages')
        return ""


class CookieCuttrAwareAnalyticsViewlet(AnalyticsViewlet):

    def render(self):
        settings = getUtility(IRegistry).forInterface(ICookieCuttrSettings)

        available = settings and settings.cookiecuttr_enabled

        # Render if CookieCuttr is enabled and Cookies were accepted
        if not available or \
            self.request.cookies.get('cc_cookie_accept', None) == \
                'cc_cookie_accept':
            return super(CookieCuttrAwareAnalyticsViewlet, self).render()
        else:
            if getattr(settings, 'implied_consent'):
                return super(CookieCuttrAwareAnalyticsViewlet, self).render()

        return ""

js_template = """
<script type="text/javascript">

    (function($) {
        $(document).ready(function () {
            if($.cookieCuttr) {
                $.cookieCuttr({cookieAnalytics: false,
                               cookiePolicyLink: "%s",
                               cookieMessage: "%s",
                               cookieAcceptButtonText: "%s",
                               cookieNotificationLocationBottom: %s
                               });
                }
        })
    })(jQuery);
</script>

"""

Introduction
============

This is an integration package for the CookieCuttr jQuery plugin.


Compatibility
=============

- Versions >= 2.0.0 are for Plone 5.2 and 6.0+.
- Versions >= 1.0.0 are for Plone 5+.
- Versions 0.7.x are for Plone 4.3.


Installation
============

Add the package name to the eggs part of your zope2 instance and rerun buildout, after a restart
you can install the package from the Modules controlpanel.


Setup
=====

The package comes with a controlpanel which is accessible through your plone_control_panel or `directly <http://localhost:8080/Plone/@@cookiecuttr-settings>`_.
Here you can enable the plugin and change some settings.

Text to show your visitor::

    We use cookies. <a href='{{cookiePolicyLink}}' title='read about our cookies'>Read everything</a

Link to page, link to the page which explains your cookiepolicy, for example ``https://plone.org`` or ``/Plone/cookies``.

Text to show in the Accept button::

    Accept if you like cookies!


Usage
=====

We need to be able to decline tracking cookies for Google Analytics; This is done by overriding the default analytics viewlet and check for cookiecuttr.

You can also wrap your own javascript code::

    if (jQuery.cookie('cc_cookie_accept') == "cc_cookie_accept") {
      ...
    }

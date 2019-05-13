.. image:: https://secure.travis-ci.org/collective/collective.cookiecuttr.png
    :target: http://travis-ci.org/collective/collective.cookiecuttr

Introduction
============

This is an integration package for the `CookieCuttr jQuery plugin`_

Versions >= 1.0.0 are for Plone 5+, if you use Plone 4.3, use versions 0.7.x.


Installation
============

Add the package name to the eggs part of your zope2 instance and rerun buildout, after a restart
you can install the package from plone_control_panel.


Setup
=====

The package comes with a controlpanel which is accessible through your plone_control_panel or `directly`_.
Here you can enable the plugin and change some settings.

Text to show your visitor

    We use cookies. <a href='{{cookiePolicyLink}}' title='read about our cookies'>Read everything</a


Link to page, link to the page which explains your cookiepolicy, for example http://plone.org or /Plone/cookies

    http://plone.org


Text to show in the Accept button

    Accept if you like cookies!


Usage
=====

We need to be able to decline tracking cookies for Google Analytics; This is done by overriding the default analytics viewlet and check for cookiecuttr.

You can also wrap your own javascript code:

    if (jQuery.cookie('cc_cookie_accept') == "cc_cookie_accept") {
    ...
    }


.. _CookieCuttr jQuery plugin: http://cookiecuttr.com/
.. _directly: http://localhost:8080/Plone/@@cookiecuttr-settings

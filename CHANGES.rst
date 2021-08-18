Changelog
=========


1.0.2 (2021-08-18)
------------------

- Fix datagrifield import.
  [odelaere]


1.0.1 (2020-01-17)
------------------

- use zope.interface.implementer instead of zope.interface.implements
  [weberc]

- Get rid of unittest2
  [gbastien]


1.0.0 (2019-05-13)
------------------

- Add Plone 5 compatibility & drop support for Plone 4
  [laulaz]


0.7.7 (2019-04-23)
------------------

- Fix text not displaying on accept button
  See fourdigits/collective.cookiecuttr#19
  [laulaz]

- Avoid useless reload of the page : cookies are working without it
  [laulaz]


0.7.6 (2018-09-07)
------------------

- Avoid displaying message multiple times
  [laulaz]


0.7.5 (2016-03-11)
------------------

- Implement option to move cookie message to the bottom
  [nightmarebadger]


0.7.4 (2014-03-31)
------------------

- When product is installed but disabled, show the standard contents
  of the analytics viewlet.
  Fixes https://github.com/fourdigits/collective.cookiecuttr/issues/5
  [maurits]


0.7.3 (2014-03-28)
------------------

- Nothing changed yet.


0.7.2 (2014-03-28)
------------------

- Uninstall profile to delete registry configuration [erral]

- Implement implied consent [erral]

- Use collective.z3cform.datagridfield and make it multilingual aware [erral]


0.7.1 (2012-11-08)
------------------

- Fix viewlet rendering, fix test [kingel]


0.7 (2012-11-08)
----------------

- Added Jan and Ralph to the contributors, thanks! [kingel]
- Started with tests [kingel]
- Travis setup [kingel]
- Added controlpanel test [kingel]
- Added support for sonar [kingel]
- Fixed viewlet rendering


0.6 (2012-10-19)
----------------

- cleaned up GA-viewlet [Jan Branbergen]
- Fix GA-viewlet when cookiecuttr is disabled [Jan Branbergen]


0.5 (2012-10-04)
----------------

- plone.resource is not used, removed dependency. Made override for anlytics viewlet [thepjot]
- javascript is not python, do not put commas at the end of arrays as it will break in ie [kingel]


0.4 (2012-09-25)
----------------

- Changed link functionality so it works with external links [ralphjacobs].


0.3 (2012-09-25)
----------------

- Nothing changed yet.


0.2 (2012-09-24)
----------------

- Nothing changed yet.


0.1 (2012-09-24)
----------------

- Package created using templer

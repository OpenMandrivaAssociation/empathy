Summary:	A IM client based on Telepathy framework
Name:		empathy
Version:	3.6.2
Release:	1
License:	LGPLv2+
Group:		Networking/Instant messaging
URL:		http://live.gnome.org/Empathy
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/3.6/%{name}-%{version}.tar.xz

BuildRequires:	glib2.0-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	iso-codes
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(champlain-gtk-0.12)
BuildRequires:	pkgconfig(cheese-gtk)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(clutter-gst-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(evolution-data-server-1.2)
BuildRequires:	pkgconfig(farstream-0.1)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(geoclue)
BuildRequires:	pkgconfig(geocode-glib)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keybindings)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.2
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mission-control-plugins)
BuildRequires:	pkgconfig(nautilus-sendto)
BuildRequires:	pkgconfig(pixman-1)
#BuildRequires:	pkgconfig(telepathy-farsight)
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(telepathy-logger-0.2)
BuildRequires:	pkgconfig(webkitgtk-3.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libsecret-1)

Requires:	folks

# anything in _datadir/glib-2.0/schemas/org.gnome.*.gschema.xml
Requires:	gsettings-desktop-schemas
Requires:	telepathy-mission-control >= 5
# jabber by default, unless someone has a better idea
Requires:	telepathy-gabble
# MD after removing dep loop in telepathy-logger
Requires:	telepathy-logger
# Spell check support
Requires:	iso-codes
# needed by MSN
Suggests:	telepathy-butterfly
# various protocol provided by libpurple
Suggests:	telepathy-haze
# needed for local XMPP
Suggests:	telepathy-salut
# needed for irc
Suggests:	telepathy-idle
# needed for voip
Suggests:	gstreamer0.10-farsight2
Suggests:	nautilus-sendto
%rename	nautilus-sendto-empathy

%description
Empathy consists of a rich set of reusable instant messaging widgets, as
well as a GNOME client that uses those widgets.

Empathy uses Telepathy and Nokia's Mission Control, and reuses Gossip's
UI. Its main goal is to integrate instant messaging with the desktop by
providing libempathy and libempathy-gtk libraries, a set of widgets that
can be embeded into any GNOME application.

%prep
%setup -q
%apply_patches

%build
%configure2_5x  \
	--disable-static \
	--enable-empathy-av=yes

%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/dbus-1/services/*
%{_bindir}/*
%{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so
%{_libdir}/nautilus-sendto/plugins/libnstempathy.so
%{_libdir}/%{name}/*.so
%{_libexecdir}/empathy-auth-client
%{_libexecdir}/empathy-call
%{_libexecdir}/empathy-chat
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/adium/message-styles/*
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml
%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_datadir}/telepathy/clients/Empathy.Call.client
%{_datadir}/telepathy/clients/Empathy.Chat.client
%{_datadir}/telepathy/clients/Empathy.FileTransfer.client
%{_mandir}/man1/*



%changelog
* Fri Nov 16 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.2-1
- update to 3.6.2

* Thu Oct 25 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.1-1
- update to 3.6.1

* Tue Oct  9 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0.3-1
- update to 3.6.0.3

* Tue Oct  9 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0.1-2
- added R: folks

* Fri Oct  5 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0.1-1
- update to 3.6.0.1

* Fri Jun 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2.3-1
+ Revision: 807603
- new version 3.4.2.3
- more spec cleanups

* Tue May 22 2012 Götz Waschk <waschk@mandriva.org> 3.4.2.1-1
+ Revision: 799992
- update to new version 3.4.2.1

* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799195
- update to new version 3.4.2

* Thu May 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.1-1
+ Revision: 795727
- BR: little version fix
- removed unneeded comment from files section
- version update 3.5.1

* Mon Jan 23 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2-2
+ Revision: 767126
- bump for BS
- fixed files list
- added missing BRs
- more spec clean up
- new version 3.2.2
- cleaned up spec
- removed .la files
- disabled static build
- removed mkrel, BuildRoot, clean section, defattr
- converted BRs to pkgcofig provides (from mga)

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 2.34.0-3
+ Revision: 686256
- tweak br
- rebuild for new webkit

* Wed May 04 2011 Funda Wang <fwang@mandriva.org> 2.34.0-2
+ Revision: 665864
- br networkmanager
- fix build with gcr 3.0
- br gnutls

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 2.34.0-1
+ Revision: 650411
- new version
- update deps
- update file list

* Thu Nov 18 2010 Götz Waschk <waschk@mandriva.org> 2.32.2-1mdv2011.0
+ Revision: 598787
- update to new version 2.32.2

* Mon Nov 15 2010 Götz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597712
- update to new version 2.32.1

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Mon Oct 18 2010 Götz Waschk <waschk@mandriva.org> 2.32.0.1-1mdv2011.0
+ Revision: 586631
- update to new version 2.32.0.1

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581338
- update to new version 2.32.0

* Mon Sep 20 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 579967
- new version
- update deps

* Thu Sep 02 2010 Götz Waschk <waschk@mandriva.org> 2.31.91.1-1mdv2011.0
+ Revision: 575248
- update to new version 2.31.91.1

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574535
- rebuild
- update build deps
- new version
- update build deps
- update file list

* Wed Aug 18 2010 Götz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 571198
- new version
- bump deps

* Mon Aug 02 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565107
- new version
- update build deps
- update file list

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2-1mdv2010.1
+ Revision: 548430
- Release 2.30.2

* Fri Jun 11 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1.1-1mdv2010.1
+ Revision: 547902
- Release 2.30.1.1

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.30.1-2mdv2010.1
+ Revision: 539612
- rebuild so that shared libraries are properly stripped again

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 539195
- update to new version 2.30.1

* Tue Apr 20 2010 Götz Waschk <waschk@mandriva.org> 2.30.0.2-1mdv2010.1
+ Revision: 537049
- update to new version 2.30.0.2

* Fri Apr 09 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.0.1-1mdv2010.1
+ Revision: 533499
- Release 2.30.0.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528805
- update to new version 2.30.0

* Mon Mar 15 2010 Götz Waschk <waschk@mandriva.org> 2.29.93-1mdv2010.1
+ Revision: 520283
- update to new version 2.29.93

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 517202
- update to new version 2.29.92

* Thu Mar 04 2010 Götz Waschk <waschk@mandriva.org> 2.29.91.2-1mdv2010.1
+ Revision: 514243
- update to new version 2.29.91.2

* Wed Mar 03 2010 Götz Waschk <waschk@mandriva.org> 2.29.91.1-1mdv2010.1
+ Revision: 513977
- update to new version 2.29.91.1

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509572
- new version
- update file list

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502713
- update to new version 2.29.90

* Mon Jan 25 2010 Götz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 496284
- update to new version 2.29.6

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 2.29.5.1-1mdv2010.1
+ Revision: 490164
- update to new version 2.29.5.1

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.29.5-2mdv2010.1
+ Revision: 489836
- bump
- update to new version 2.29.5

* Wed Dec 30 2009 Pascal Terjan <pterjan@mandriva.org> 2.29.4-2mdv2010.1
+ Revision: 483990
- Update BuildRequires

* Mon Dec 21 2009 Götz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 480919
- new version
- add nautilus-sendto plugin

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475386
- new version
- drop library packages
- update file list

* Sat Nov 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.1.2-1mdv2010.1
+ Revision: 467794
- update to new version 2.28.1.2

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 2.28.1.1-1mdv2010.1
+ Revision: 460932
- new version
- drop patch

* Sun Oct 25 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-2mdv2010.0
+ Revision: 459223
- Patch0: various bugfixes from GIT

* Tue Oct 20 2009 Götz Waschk <waschk@mandriva.org> 2.28.1-1mdv2010.0
+ Revision: 458337
- update to new version 2.28.1

* Fri Oct 02 2009 Götz Waschk <waschk@mandriva.org> 2.28.0.1-1mdv2010.0
+ Revision: 452740
- new version
- drop patch

* Tue Sep 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.0-2mdv2010.0
+ Revision: 447371
- Replace patch1 with upstream solution (patch0)
- Add suggests for telepathy-salut (local xmpp) and gstreamer0.10-farsight2 (voip)

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446843
- new version
- drop patch
- fix linking

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-2mdv2010.0
+ Revision: 441070
- patch for new libchamplain

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437183
- new version
- drop patch
- new major

* Tue Sep 01 2009 Götz Waschk <waschk@mandriva.org> 2.27.91.1-2mdv2010.0
+ Revision: 423635
- fix pkgconfig file
- update deps

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 2.27.91.1-1mdv2010.0
+ Revision: 421342
- new version
- new major
- enable geoclue support
- update file list

* Wed Jul 29 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 403981
- new version
- new majors

* Wed Jul 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 396279
- update to new version 2.27.4

  + Frederik Himpe <fhimpe@mandriva.org>
    - Empathy now uses enchant for spell check, so adapt BuildRequires accordingly
    - Enable Adium theme support (BuildRequires: libwebkitgtk-devel)

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386079
- new version
- new major

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379702
- new version
- new major

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 2.27.1.1-1mdv2010.0
+ Revision: 377542
- new version
- new major

* Mon May 18 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 376888
- new version
- new major

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366958
- update to new version 2.26.1

* Mon Mar 30 2009 Götz Waschk <waschk@mandriva.org> 2.26.0.1-1mdv2009.1
+ Revision: 362596
- new version

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355998
- new version
- new major

* Tue Mar 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 348065
- new version
- new major
- remove old configure options

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341275
- new version
- new major

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336843
- new version
- update deps
- new major

* Sat Jan 10 2009 Götz Waschk <waschk@mandriva.org> 2.25.4-2mdv2009.1
+ Revision: 328026
- fix deps of the devel package

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 326165
- new version
- update build deps

* Wed Dec 31 2008 Adam Williamson <awilliamson@mandriva.org> 2.25.3-2mdv2009.1
+ Revision: 321623
- rebuild with python 2.6

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315745
- new version
- new major

* Mon Dec 01 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-2mdv2009.1
+ Revision: 308803
- bump release
- disable werror to make it build on x86_64
- fix buildrequires
- new version
- new major

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.24.1-2mdv2009.1
+ Revision: 301578
- rebuilt against new libxcb

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295914
- update to new version 2.24.1

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286838
- new version

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 283081
- new version

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278104
- new version
- new major
- fix build deps

* Tue Aug 19 2008 Frederik Himpe <fhimpe@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 274018
- Update to new version 2.23.90
- Suggest telepathy-haze, telepathy-stream-engine and telepathy-butterfly

* Mon Aug 04 2008 Frederik Himpe <fhimpe@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263607
- Update to new upstream version 0.23.6
- Don't run autogen.sh: it's not necessary anymore and it breaks build
- Add new desktop file

* Wed Jul 16 2008 Michael Scherer <misc@mandriva.org> 0.23.4-1mdv2009.0
+ Revision: 236524
- update to 0.23.4
- make Source line compatible with mdvsys update

* Wed Jul 09 2008 Michael Scherer <misc@mandriva.org> 0.23.3-1mdv2009.0
+ Revision: 232930
- add missing BuildRequires
- update to 0.23.3

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 17 2008 Frederik Himpe <fhimpe@mandriva.org> 0.22.1-2mdv2009.0
+ Revision: 195435
- Add various fixes from svn:
  * Hide sound preferences: upstream did not yet implement
    sound notifications
  * Do not start Empathy automatically at log in: instead use
    a standard desktop file with the right categories
  * Make nothere applet removable
  * Make nothere applet find status icons
  * Various important crash fixes

  + Funda Wang <fwang@mandriva.org>
    - add GNOME menu category

* Tue Apr 15 2008 Funda Wang <fwang@mandriva.org> 0.22.1-1mdv2009.0
+ Revision: 194015
- New version 0.22.1

* Mon Mar 10 2008 Michael Scherer <misc@mandriva.org> 0.22.0-1mdv2008.1
+ Revision: 183426
- new version 0.22

* Thu Mar 06 2008 Michael Scherer <misc@mandriva.org> 0.21.91-2mdv2008.1
+ Revision: 180346
- activate voip

* Tue Mar 04 2008 Michael Scherer <misc@mandriva.org> 0.21.91-1mdv2008.1
+ Revision: 178262
- add missing buildrequires
- new version, just before version freeze

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 0.21.90-1mdv2008.1
+ Revision: 164717
- New version 0.21.90

* Thu Jan 17 2008 Michael Scherer <misc@mandriva.org> 0.21.5.2-1mdv2008.1
+ Revision: 154098
- new major of the gtk library
- new version of empathy

* Sat Jan 05 2008 Jérôme Soyer <saispo@mandriva.org> 0.21.4-1mdv2008.1
+ Revision: 145805
- Add files
- New release
- New release

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 28 2007 Funda Wang <fwang@mandriva.org> 0.21.1-1mdv2008.1
+ Revision: 102887
- new major
- New version 0.21.1

* Tue Oct 16 2007 Michael Scherer <misc@mandriva.org> 0.14-2mdv2008.1
+ Revision: 99004
- add NotHere applet ( even if disabled by default because it cannot be removed )
- split python from main package
- add megaphone applet
- correctly list python module on x86_64

  + Pascal Terjan <pterjan@mandriva.org>
    - Update major

  + Jérôme Soyer <saispo@mandriva.org>
    - New release
    - New release

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.12-3mdv2008.0
+ Revision: 81781
- fix build deps

  + Michael Scherer <misc@mandriva.org>
    - rebuild for new mission control
    - add python binding

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Aug 27 2007 Michael Scherer <misc@mandriva.org> 0.12-1mdv2008.0
+ Revision: 71803
- new version

* Mon Aug 13 2007 Funda Wang <fwang@mandriva.org> 0.11-1mdv2008.0
+ Revision: 62398
- split gtk lib, so that different major lib could be co-exists
- New version 0.11

* Tue Jul 31 2007 Funda Wang <fwang@mandriva.org> 0.10-1mdv2008.0
+ Revision: 56837
- BR libgcrypt
- New version 0.10

* Thu Jul 26 2007 Funda Wang <fwang@mandriva.org> 0.9-1mdv2008.0
+ Revision: 55812
- fix rpm group
- Introduce lib and devel sub package
- New version 0.9

* Mon Jun 25 2007 Michael Scherer <misc@mandriva.org> 0.8-1mdv2008.0
+ Revision: 43885
- new version

* Sat Jun 09 2007 Michael Scherer <misc@mandriva.org> 0.7-1mdv2008.0
+ Revision: 37721
- verson 0.7

* Sat Jun 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6-1mdv2008.0
+ Revision: 34763
- New version 0.6
- Remove X-MandrivaLinux-* keyword from category

* Tue May 29 2007 Michael Scherer <misc@mandriva.org> 0.5-2mdv2008.0
+ Revision: 32270
- add missing Requires, and pull jabber by default
- new desc proposed by John Keller

* Mon May 28 2007 Michael Scherer <misc@mandriva.org> 0.5-1mdv2008.0
+ Revision: 31983
- new version

* Wed May 23 2007 Michael Scherer <misc@mandriva.org> 0.4-1mdv2008.0
+ Revision: 30451
- add missing BuildRequires
- add menui file
- Import empathy


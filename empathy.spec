Summary: A IM client based on Telepathy framework
Name: empathy
Version: 2.31.6
Release: %mkrel 1
License: LGPLv2+
Group: Networking/Instant messaging
URL: http://live.gnome.org/Empathy
Source: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: libGConf2-devel
BuildRequires: libtelepathy-farsight-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: gtk+2-devel
BuildRequires: libcanberra-devel
BuildRequires: unique-devel
BuildRequires: libfolks-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libnotify-devel
BuildRequires: libtelepathy-glib-devel >= 0.11.7
BuildRequires: libtelepathy-logger-devel
BuildRequires: evolution-data-server-devel
BuildRequires: nautilus-sendto-devel
BuildRequires: intltool
BuildRequires: libgcrypt-devel
BuildRequires: gtk-doc
# Spell check support
BuildRequires: iso-codes
BuildRequires: enchant-devel
# Adium support
Buildrequires: libwebkitgtk-devel
BuildRequires: libgeoclue-devel
BuildRequires: libchamplain-devel

BuildRequires: libxslt-proc
BuildRequires: gnome-doc-utils >= 0.17.3
Requires: telepathy-mission-control >= 5
# jabber by default, unless someone as a better idea
Requires: telepathy-gabble
# needed by MSN
Suggests: telepathy-butterfly
# various protocol provided by libpurple
Suggests: telepathy-haze
# needed for local XMPP
Suggests: telepathy-salut
# needed for irc
Suggests: telepathy-idle
# needed for voip
Suggests: gstreamer0.10-farsight2
Suggests: nautilus-sendto
Provides: nautilus-sendto-empathy
Obsoletes: nautilus-sendto-empathy

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
Empathy consists of a rich set of reusable instant messaging widgets, as
well as a GNOME client that uses those widgets.

Empathy uses Telepathy and Nokia's Mission Control, and reuses Gossip's
UI. Its main goal is to integrate instant messaging with the desktop by
providing libempathy and libempathy-gtk libraries, a set of widgets that
can be embeded into any GNOME application.


%prep
%setup -q

%build
%configure2_5x --enable-gtk3=no
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/nautilus-sendto/plugins/libnstempathy*a

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS
%_datadir/icons/hicolor/*/apps/*
%_datadir/dbus-1/services/*
%_bindir/*
%_datadir/%{name}/*
%_datadir/telepathy/clients/Empathy.client
%_datadir/telepathy/clients/Empathy.AudioVideo.client
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-accounts.desktop
%{_mandir}/man1/*
#%{_datadir}/omf/%{name}/*.omf
%_libdir/nautilus-sendto/plugins/libnstempathy.so
%_libexecdir/empathy-av
%_datadir/GConf/gsettings/empathy.convert
%_datadir/glib-2.0/schemas/org.gnome.Empathy.gschema.xml

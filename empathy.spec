Summary: A IM client based on Telepathy framework
Name: empathy
Version: 3.2.2
Release: 1
License: LGPLv2+
Group: Networking/Instant messaging
URL: http://live.gnome.org/Empathy
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-doc-utils >= 0.17.3
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(champlain-gtk-0.12)
BuildRequires:	pkgconfig(cheese-gtk) >= 2.91.91.1
BuildRequires:	pkgconfig(clutter-1.0) >= 1.7.14
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(clutter-gst-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant) >= 1.2.0
BuildRequires:	pkgconfig(evolution-data-server-1.2)
BuildRequires:	pkgconfig(farsight2-0.10)
BuildRequires:	pkgconfig(folks) >= 0.6.0
BuildRequires:	pkgconfig(gcr-3) >= 2.91.4
BuildRequires:	pkgconfig(geoclue) >= 0.11
BuildRequires:	pkgconfig(geocode-glib)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gnome-keybindings) >= 2.31.4
BuildRequires:	pkgconfig(gnome-keyring-1) >= 2.26.0
BuildRequires:	pkgconfig(gnutls) >= 2.8.5
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gstreamer-0.10) >= 0.10.32
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.2
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.25
BuildRequires:	pkgconfig(libnm-glib) >= 0.7.0
BuildRequires:	pkgconfig(libnotify) >= 0.7
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(nautilus-sendto) >= 2.90.0
BuildRequires:	pkgconfig(telepathy-farsight) >= 0.0.18
BuildRequires:	pkgconfig(telepathy-farstream) >= 0.1.2
BuildRequires:	pkgconfig(telepathy-glib) >= 0.17.0
BuildRequires:	pkgconfig(telepathy-logger-0.2) >= 0.2.10
BuildRequires:	pkgconfig(webkitgtk-3.0) >= 1.3.13
BuildRequires:	pkgconfig(x11)

# anything in _datadir/glib-2.0/schemas/org.gnome.*.gschema.xml
Requires:	gsettings-desktop-schemas
Requires:	telepathy-mission-control >= 5
# jabber by default, unless someone has a better idea
Requires:	telepathy-gabble
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
Provides:	nautilus-sendto-empathy
Obsoletes:	nautilus-sendto-empathy

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
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/dbus-1/services/*
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/telepathy/clients/Empathy.client
%{_datadir}/telepathy/clients/Empathy.AudioVideo.client
%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_datadir}/telepathy/clients/Empathy.Call.client
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-accounts.desktop
%{_mandir}/man1/*
%{_libdir}/nautilus-sendto/plugins/libnstempathy.so
%_libexecdir/empathy-av
%_libexecdir/empathy-auth-client
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml

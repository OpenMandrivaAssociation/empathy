Summary: A IM client based on Telepathy framework
Name: empathy
Version: 3.4.1
Release: 1
License: LGPLv2+
Group: Networking/Instant messaging
URL: http://live.gnome.org/Empathy
Source0: http://ftp.gnome.org/pub/GNOME/sources/empathy/%{name}-%{version}.tar.xz

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
BuildRequires:	pkgconfig(telepathy-farsight)
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(telepathy-logger-0.2)
BuildRequires:	pkgconfig(webkitgtk-3.0)
BuildRequires:	pkgconfig(x11)

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

for l in C ca cs de el en_GB es eu fi fr gl hu it ja lv pl ru sl sv te zh_CN; do
	echo "%%dir %%{_datadir}/help/$l"
	echo "%%lang($l) %%{_datadir}/help/$l/%%{name}"
done >> %{name}.lang

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/dbus-1/services/*
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/telepathy/clients/Empathy.AudioVideo.client
%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_datadir}/telepathy/clients/Empathy.Call.client
%{_datadir}/telepathy/clients/Empathy.Chat.client
%{_datadir}/telepathy/clients/Empathy.FileTransfer.client
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-accounts.desktop
%{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so
%{_libdir}/nautilus-sendto/plugins/libnstempathy.so
%{_libexecdir}/empathy-av
%{_libexecdir}/empathy-auth-client
%{_libexecdir}/empathy-call
%{_libexecdir}/empathy-chat
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml
%{_mandir}/man1/*

#{_datadir}/help/*/%{name}/*.page
#{_datadir}/help/*/%{name}/figures/*.png

Summary: A IM client based on Telepathy framework
Name: empathy
Version: 0.9
Release: %mkrel 1
License: GPL
Group: Networking/Instant messaging
URL: http://live.gnome.org/Empathy
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libtelepathy)
BuildRequires: pkgconfig(libmissioncontrol)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: intltool
Requires: telepathy-mission-control
# jabber by default, unless someone as a better idea
Requires: telepathy-gabble

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
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name} --with-gnome
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Empathy
Comment=Instant messaging client
Exec=%_bindir/empathy
Icon=%{name}
Terminal=false
Type=Application
Categories=Network;InstantMessaging;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas %{name}

%post
%post_install_gconf_schemas %{schemas}
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %{schemas}

%postun
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS
%{_sysconfdir}/gconf/schemas/*
%_datadir/icons/hicolor/*/apps/*
%_datadir/dbus-1/services/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_bindir/*
%_datadir/%{name}/*
%_datadir/gnome/autostart/%{name}.desktop
%_datadir/telepathy/managers/*
%_datadir/mission-control/profiles/*

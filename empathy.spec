%define libname %mklibname %name 0
%define develname %mklibname -d %name

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
Requires: %{libname} = %{version}-%{release}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
Empathy consists of a rich set of reusable instant messaging widgets, as
well as a GNOME client that uses those widgets.

Empathy uses Telepathy and Nokia's Mission Control, and reuses Gossip's
UI. Its main goal is to integrate instant messaging with the desktop by
providing libempathy and libempathy-gtk libraries, a set of widgets that
can be embeded into any GNOME application.

%package -n %{libname}
Summary: Libraries for %{name}
Group: System/Libraries

%description -n %{libname}
This package contains library files for %{name}.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%package -n %{develname}
Summary: Developement files for %{name}
Group: Development/GNOME and GTK+
Requires: %{libname} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains developement files for %{name}.

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
%update_menus

%preun
%preun_uninstall_gconf_schemas %{schemas}

%postun
%clean_menus
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

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libempathy-gtk
%{_includedir}/libempathy
%{_datadir}/gtk-doc/html/libempathy-gtk
%{_datadir}/gtk-doc/html/libempathy

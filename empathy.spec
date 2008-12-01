%define major 17
%define libname %mklibname %name %major
%define gtkmajor 15
%define gtklibname %mklibname %name-gtk %gtkmajor
%define develname %mklibname -d %name

Summary: A IM client based on Telepathy framework
Name: empathy
Version: 2.25.2
Release: %mkrel 2
License: LGPLv2+
Group: Networking/Instant messaging
URL: http://live.gnome.org/Empathy
Source: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: libGConf2-devel
BuildRequires: libtelepathy-devel
BuildRequires: telepathy-mission-control-devel
BuildRequires: gtk+2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnomeui2-devel
BuildRequires: evolution-data-server-devel
BuildRequires: intltool
BuildRequires: libgcrypt-devel
# Required for patch1:
BuildRequires: gnome-common
BuildRequires: gtk-doc
# required by aspell
BuildRequires: iso-codes
BuildRequires: aspell-devel
# for python binding
BuildRequires: python-devel
BuildRequires: pygtk2.0-devel
# for applet
BuildRequires: gnome-panel-devel
BuildRequires: libxslt-proc
BuildRequires: gnome-doc-utils
#gw libtool dep:
BuildRequires: libtasn1-devel
Requires: telepathy-mission-control
# jabber by default, unless someone as a better idea
Requires: telepathy-gabble
Suggests: telepathy-butterfly
Suggests: telepathy-haze
Suggests: telepathy-stream-engine
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
Obsoletes: %mklibname %name 0

%description -n %{libname}
This package contains library files for %{name}.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%package -n %{gtklibname}
Summary: Libraries for %{name}-gtk
Group: System/Libraries
Obsoletes: %mklibname %name 0

%description -n %{gtklibname}
This package contains library files for %{name}-gtk.

%if %mdkversion < 200900
%post -n %{gtklibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{gtklibname} -p /sbin/ldconfig
%endif

%package -n %{develname}
Summary: Developement files for %{name}
Group: Development/GNOME and GTK+
Requires: %{libname} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains developement files for %{name}.

%package -n python-%name
Summary: Python module for %{name}
Group: Development/Python

%description -n python-%name
This package contains the python module for %{name}.

%prep
%setup -q

%build
%configure2_5x --enable-python=yes --enable-aspell=yes --enable-nothere=yes --enable-voip=yes --with-compile-warnings=no

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name} --with-gnome

rm -Rf $RPM_BUILD_ROOT/%py_platsitedir/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas %{name}

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %{schemas}
%update_icon_cache hicolor
%update_menus
%endif

%preun
%preun_uninstall_gconf_schemas %{schemas}

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS
%{_sysconfdir}/gconf/schemas/*
%_datadir/icons/hicolor/*/apps/*
#%_datadir/dbus-1/services/*
%_bindir/*
%_datadir/%{name}/*
#%_datadir/telepathy/managers/*
%_datadir/mission-control/profiles/*
%{_datadir}/applications/%{name}.desktop
%_libdir/megaphone-applet
%_libdir/bonobo/servers/GNOME_Megaphone_Applet.server
%_libdir/bonobo/servers/GNOME_NotHere_Applet.server
%_libdir/nothere-applet
#%{_libdir}/empathy-call-chandler
%{_mandir}/man1/*
%{_datadir}/omf/%{name}/*.omf


%files -n python-%{name}
%defattr(-,root,root)
%py_platsitedir/*so

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libempathy.so.%{major}*

%files -n %{gtklibname}
%defattr(-,root,root)
%{_libdir}/libempathy-gtk.so.%{gtkmajor}*

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

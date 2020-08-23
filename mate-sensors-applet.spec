%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	0
%define libname	%mklibname %{name}-plugin %{major}
%define devname	%mklibname -d %{name}-plugin

Summary:	Detailed hardware monitoring applet for MATE
Name:		mate-sensors-applet
Version:	1.24.1
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Other
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		mate-sensors-applet-1.20.3-fix-linkage.patch

BuildRequires:	autoconf-archive
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	lm_sensors-devel
BuildRequires:  pkgconfig(cairo) >= 1.0.4
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(udisks2)
BuildRequires:	xsltproc
BuildRequires:	yelp-tools

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

MATE Sensors Applet is an applet for the MATE Panel to display readings from
hardware sensors, including CPU temperature, fan speeds and voltage readings
under Linux.

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/mate-sensors-applet/plugins/libacpi.so
%{_libdir}/mate-sensors-applet/plugins/libaticonfig.so
%{_libdir}/mate-sensors-applet/plugins/libhddtemp.so
%{_libdir}/mate-sensors-applet/plugins/libi8k.so
%{_libdir}/mate-sensors-applet/plugins/libibm-acpi.so
%{_libdir}/mate-sensors-applet/plugins/libomnibook.so
%{_libdir}/mate-sensors-applet/plugins/libpmu-sys.so
%{_libdir}/mate-sensors-applet/plugins/libsmu-sys.so
%{_libdir}/mate-sensors-applet/plugins/liblibsensors.so
%{_libdir}/mate-sensors-applet/plugins/libsonypi.so
%{_libdir}/mate-sensors-applet/plugins/libmbmon.so
%{_libdir}/mate-sensors-applet/plugins/libudisks2.so
%{_datadir}/dbus-1/services/org.mate.panel.applet.SensorsAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.sensor.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.SensorsApplet.mate-panel-applet
%{_datadir}/mate-sensors-applet/ui/SensorsApplet.xml
%{_libexecdir}/mate-sensors-applet
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/*/*.png

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	mate-sensors-applet libraries
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries used by %{name}.

%files -n %{libname}
%{_libdir}/libmate-sensors-applet-plugin.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for mate-sensors-applet
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and includes files for developing programs
based on %{name}.

%files -n %{devname}
%{_includedir}/mate-sensors-applet/*
%{_libdir}/*.so

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--enable-libnotify \
	--with-nvidia \
	--with-aticonfig \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

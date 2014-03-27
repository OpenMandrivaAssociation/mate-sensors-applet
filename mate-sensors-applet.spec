%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	0
%define libname	%mklibname %{name}-plugin %{major}
%define devname	%mklibname -d %{name}-plugin

Summary:	Detailed hardware monitoring applet for MATE
Name:		mate-sensors-applet
Version:	1.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		sensors-applet-2.2.3-fix-linkage.patch
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	lm_sensors-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)

%description
MATE Sensors Applet is an applet for the MATE Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds and
voltage readings under Linux.

Interfaces via the Linux kernel i2c modules.

%package -n %{libname}
Summary:	mate-sensors-applet libraries
Group:		System/Libraries

%description -n %{libname}
This is the shared library parts of %{name}.

%package -n %{devname}
Summary:	Development files for mate-sensors-applet
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files for mate-sensors-applet.

%prep
%setup -q
%apply_patches
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x \
	--disable-static \
	--enable-libnotify \
	--with-nvidia

%make

%install
mkdir -p %{buildroot}%{_libdir}/mate-sensors-applet
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/mate-sensors-applet/plugins/libacpi.so
%{_libdir}/mate-sensors-applet/plugins/libaticonfig.so
%{_libdir}/mate-sensors-applet/plugins/libeee.so
%{_libdir}/mate-sensors-applet/plugins/libhddtemp.so
%{_libdir}/mate-sensors-applet/plugins/libi8k.so
%{_libdir}/mate-sensors-applet/plugins/libibm-acpi.so
%{_libdir}/mate-sensors-applet/plugins/libomnibook.so
%{_libdir}/mate-sensors-applet/plugins/libpmu-sys.so
%{_libdir}/mate-sensors-applet/plugins/libsmu-sys.so
%{_libdir}/mate-sensors-applet/plugins/liblibsensors.so
%{_libdir}/mate-sensors-applet/plugins/libsonypi.so
%{_datadir}/dbus-1/services/org.mate.panel.applet.SensorsAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.sensor.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.sensors-applet.mate-panel-applet
%{_datadir}/mate-sensors-applet/ui/SensorsApplet.xml
%{_libexecdir}/mate-sensors-applet
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/*/*.png

%files -n %{libname}
%{_libdir}/libmate-sensors-applet-plugin.so.%{major}*

%files -n %{devname}
%{_includedir}/mate-sensors-applet/*
%{_libdir}/*.so


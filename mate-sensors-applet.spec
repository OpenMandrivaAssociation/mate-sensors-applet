Summary:	Detailed hardware monitoring applet for MATE
Name:		mate-sensors-applet
Version:	1.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
Patch0:		sensors-applet-2.2.3-fix-linkage.patch
Patch1:		mate-sensors-applet-1.2.0-fixlibdir.patch

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(libmateui-2.0)
BuildRequires:	pkgconfig(libmatepanelapplet-2.0)

%description
MATE Sensors Applet is an applet for the MATE Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds and
voltage readings under Linux.

Interfaces via the Linux kernel i2c modules.

%package	devel
Summary:	Development files for mate-sensors-applet
Group:		Development/Other
Requires:	%{name} = %{version}

%description devel
This package contains development files for mate-sensors-applet.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--enable-libmatenotify \
	--without-libsensors

%make LIBS='-ldl -lgtk-x11-2.0 -lgdk-x11-2.0 -lcairo -lgdk_pixbuf-2.0 -lgobject-2.0 -lglib-2.0 -lmatecomponent-2 -lmatecomponent-activation -lmate-panel-applet-2 -lmateconf-2 -lmate-2 -lmatenotify'

%install
mkdir -p %{buildroot}%{_libdir}/mate-sensors-applet
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/*.so.0*
%{_libexecdir}/mate-sensors-applet
%{_libexecdir}/matecomponent/servers/SensorsApplet.server
%{_datadir}/pixmaps/*
%{_datadir}/mate-2.0/ui/SensorsApplet.xml
%{_iconsdir}/hicolor/*/*/*.png
# mate help files
%{_datadir}/mate/help

%files devel
%{_includedir}/mate-sensors-applet/*
%{_libdir}/*.so


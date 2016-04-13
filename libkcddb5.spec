%define major 5
%define libname %mklibname kcddb %{major}
%define devname %mklibname kcddb -d
%define wlibname %mklibname kcddbwidgets %{major}
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20160413

Name:		libkcddb5
Version:	5.21.0
Release:	1
%if 0%git
# Taken from kf5 branch of git://anongit.kde.org/libkcddb.git
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
%endif
Summary:	CDDB database library for KDE Frameworks 5
URL:		http://kde.org/
License: 	LGPL
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	ninja
Requires: %{libname} = %{EVRD}
Requires: %{wlibname} = %{EVRD}

%description
CDDB database library for KDE Frameworks 5

%package -n %{libname}
Summary: CDDB database library for KDE Frameworks 5
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
CDDB database library for KDE Frameworks 5

%package -n %{wlibname}
Summary: CDDB database library for KDE Frameworks 5 (GUI components)
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{wlibname}
CDDB database library for KDE Frameworks 5 (GUI components)

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{wlibname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%if 0%git
%setup -qn %{name}
%else
%setup -q
%endif
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/config.kcfg/libkcddb.kcfg
%{_datadir}/kservices5/libkcddb.desktop
%{_libdir}/qt5/plugins/kcm_cddb.so
%doc %{_docdir}/HTML/en/kcontrol/cddbretrieval

%files -n %{libname}
%{_libdir}/libkcddb.so.%{major}*

%files -n %{wlibname}
%{_libdir}/libkcddbwidgets.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/libkcddb

#
# Conditional build:
%bcond_without	gtk2		# GTK+2 API
%bcond_without	gtk3		# GTK+3 API
# reenable when new babl/gegl will arrive that actually is able to build
%bcond_with	introspection	# API introspection
# reenable when new babl/gegl will arrive that actually is able to build
%bcond_with	vala		# Vala API
#
%if %{without introspection}
%undefine	with_vala
%endif
Summary:	Utility library for using GEGL in GTK+ based applications
Summary(pl.UTF-8):	Biblioteka narzędziowa do używania biblioteki GEGL w aplikacjach opartych na GTK+
Name:		gegl-gtk
Version:	0.0.7
Release:	4
License:	LGPL v3+
Group:		Libraries
Source0:	ftp://ftp.gimp.org/pub/gegl-gtk/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	646b2cf05a636ece6d55a9ba7d179361
# git diff 0.0.7 c0ea020056feeed9edff5fbf2b812c5606366d9e (before switch to gegl 0.3)
# (then adjusted to apply on dist tarball)
Patch0:		%{name}-git.patch
URL:		http://www.gegl.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.6
BuildRequires:	babl-devel >= 0.1.4
%{?with_introspection:BuildRequires:	/usr/share/gir-1.0/Gegl-0.2.gir}
BuildRequires:	cairo-gobject-devel
BuildRequires:	gegl-devel >= 0.2.0
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk+3-devel >= 3.0.0
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 0.10.0}
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
%{?with_vala:BuildRequires:	vala}
Requires:	babl >= 0.1.4
Requires:	gegl >= 0.2.0
Requires:	glib2 >= 1:2.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility library for using GEGL in GTK+ based applications.

%description -l pl.UTF-8
Biblioteka narzędziowa do używania biblioteki GEGL w aplikacjach
opartych na GTK+.

%package -n gegl-gtk2
Summary:	Utility library for using GEGL in GTK+ 2 based applications
Summary(pl.UTF-8):	Biblioteka narzędziowa do używania biblioteki GEGL w aplikacjach opartych na GTK+ 2
Group:		Libraries
Requires:	babl >= 0.1.4
Requires:	gegl >= 0.2.0
Requires:	glib2 >= 1:2.22.0
Requires:	gtk+2 >= 2:2.18.0

%description -n gegl-gtk2
Utility library for using GEGL in GTK+ 2 based applications.

%description -n gegl-gtk2 -l pl.UTF-8
Biblioteka narzędziowa do używania biblioteki GEGL w aplikacjach
opartych na GTK+ 2.

%package -n gegl-gtk2-devel
Summary:	Header files for gegl-gtk2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gegl-gtk2
Group:		Development/Libraries
Requires:	gegl-gtk2 = %{version}-%{release}
Requires:	babl-devel >= 0.1.4
Requires:	gegl-devel >= 0.2.0
Requires:	glib2-devel >= 1:2.22.0
Requires:	gtk+2-devel >= 2:2.18.0

%description -n gegl-gtk2-devel
Header files for gegl-gtk2 library.

%description -n gegl-gtk2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gegl-gtk2.

%package -n gegl-gtk2-static
Summary:	Static gegl-gtk2 library
Summary(pl.UTF-8):	Statyczna biblioteka gegl-gtk2
Group:		Development/Libraries
Requires:	gegl-gtk2-devel = %{version}-%{release}

%description -n gegl-gtk2-static
Static gegl-gtk2 library.

%description -n gegl-gtk2-static -l pl.UTF-8
Statyczna biblioteka gegl-gtk2.

%package -n vala-gegl-gtk2
Summary:	Vala API for gegl-gtk2 library
Summary(pl.UTF-8):	API języka Vala dla biblioteki gegl-gtk2
Group:		Development/Libraries
Requires:	gegl-gtk2-devel = %{version}-%{release}
Requires:	vala-gegl >= 0.2.0

%description -n vala-gegl-gtk2
Vala API for gegl-gtk2 library.

%description -n vala-gegl-gtk2 -l pl.UTF-8
API języka Vala dla biblioteki gegl-gtk2.

%package -n gegl-gtk3
Summary:	Utility library for using GEGL in GTK+ 3 based applications
Summary(pl.UTF-8):	Biblioteka narzędziowa do używania biblioteki GEGL w aplikacjach opartych na GTK+ 3
Group:		Libraries
Requires:	babl >= 0.1.4
Requires:	gegl >= 0.2.0
Requires:	glib2 >= 1:2.22.0
Requires:	gtk+3 >= 3.0.0

%description -n gegl-gtk3
Utility library for using GEGL in GTK+ 3 based applications.

%description -n gegl-gtk3 -l pl.UTF-8
Biblioteka narzędziowa do używania biblioteki GEGL w aplikacjach
opartych na GTK+ 3.

%package -n gegl-gtk3-devel
Summary:	Header files for gegl-gtk3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gegl-gtk3
Group:		Development/Libraries
Requires:	gegl-gtk3 = %{version}-%{release}
Requires:	babl-devel >= 0.1.4
Requires:	gegl-devel >= 0.2.0
Requires:	glib2-devel >= 1:2.22.0
Requires:	gtk+3-devel >= 3.0.0

%description -n gegl-gtk3-devel
Header files for gegl-gtk3 library.

%description -n gegl-gtk3-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gegl-gtk3.

%package -n gegl-gtk3-static
Summary:	Static gegl-gtk3 library
Summary(pl.UTF-8):	Statyczna biblioteka gegl-gtk3
Group:		Development/Libraries
Requires:	gegl-gtk3-devel = %{version}-%{release}

%description -n gegl-gtk3-static
Static gegl-gtk3 library.

%description -n gegl-gtk3-static -l pl.UTF-8
Statyczna biblioteka gegl-gtk3.

%package -n vala-gegl-gtk3
Summary:	Vala API for gegl-gtk3 library
Summary(pl.UTF-8):	API języka Vala dla biblioteki gegl-gtk3
Group:		Development/Libraries
Requires:	gegl-gtk3-devel = %{version}-%{release}
Requires:	vala-gegl >= 0.2.0

%description -n vala-gegl-gtk3
Vala API for gegl-gtk3 library.

%description -n vala-gegl-gtk3 -l pl.UTF-8
API języka Vala dla biblioteki gegl-gtk3.

%package apidocs
Summary:	gegl library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gegl
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gegl library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gegl.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
for d in %{?with_gtk2:2.0} %{?with_gtk3:3.0} ; do
install -d build-gtk${d}
cd build-gtk${d}
../%configure \
	%{!?with_introspection:--disable-introspection} \
	--disable-silent-rules \
	--enable-static \
	--with-gtk=${d} \
	--with-html-dir=%{_gtkdocdir} \
	--with-vala%{!?with_vala:=no}
%{__make}
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

for d in %{?with_gtk2:2.0} %{?with_gtk3:3.0} ; do
%{__make} -C build-gtk${d} install \
	DESTDIR=$RPM_BUILD_ROOT
done

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gegl-0.2/*.{a,la}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgegl-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n gegl-gtk2 -p /sbin/ldconfig
%postun	-n gegl-gtk2 -p /sbin/ldconfig

%post	-n gegl-gtk3 -p /sbin/ldconfig
%postun	-n gegl-gtk3 -p /sbin/ldconfig

%if %{with gtk2}
%files -n gegl-gtk2
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libgegl-gtk2-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-gtk2-0.1.so.0
%attr(755,root,root) %{_libdir}/gegl-0.2/gegl-gtk2-display.so
%{?with_introspection:%{_libdir}/girepository-1.0/GeglGtk2-0.1.typelib}

%files -n gegl-gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-gtk2-0.1.so
%{_includedir}/gegl-gtk2-0.1
%{?with_introspection:%{_datadir}/gir-1.0/GeglGtk2-0.1.gir}
%{_pkgconfigdir}/gegl-gtk2-0.1.pc

%files -n gegl-gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libgegl-gtk2-0.1.a

%if %{with vala}
%files -n vala-gegl-gtk2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gegl-gtk2-0.1.deps
%{_datadir}/vala/vapi/gegl-gtk2-0.1.vapi
%endif
%endif

%if %{with gtk3}
%files -n gegl-gtk3
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libgegl-gtk3-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-gtk3-0.1.so.0
%attr(755,root,root) %{_libdir}/gegl-0.2/gegl-gtk3-display.so
%{?with_introspection:%{_libdir}/girepository-1.0/GeglGtk3-0.1.typelib}

%files -n gegl-gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-gtk3-0.1.so
%{_includedir}/gegl-gtk3-0.1
%{?with_introspection:%{_datadir}/gir-1.0/GeglGtk3-0.1.gir}
%{_pkgconfigdir}/gegl-gtk3-0.1.pc

%files -n gegl-gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libgegl-gtk3-0.1.a

%if %{with vala}
%files -n vala-gegl-gtk3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gegl-gtk3-0.1.deps
%{_datadir}/vala/vapi/gegl-gtk3-0.1.vapi
%endif
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gegl-gtk-%{version}
%endif

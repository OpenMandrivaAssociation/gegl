%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1

%global optflags %{optflags} -O3

%define api 0.4
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libsc %mklibname %{name}-sc %{api}
%define libnpd %mklibname %{name}-npd %{api}
%define devname %mklibname -d %{name} %{api}
%define	girname	%mklibname %{name}-gir %{api}

Summary:	GEGL (Generic Graphics Library) - graph based image processing framework
Name:		gegl
Version:	0.4.48
Release:	1
Group:		System/Libraries
License:	LGPLv3+
Url:		https://www.gegl.org/
# git clone git://git.gnome.org/gegl
Source0:	https://download.gimp.org/pub/gegl/%{api}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	enscript
BuildRequires:	intltool
BuildRequires:	graphviz
BuildRequires:	imagemagick
BuildRequires:  librsvg2
BuildRequires:	pango-modules
BuildRequires:	perl-devel
BuildRequires:	python-gobject-introspection
BuildRequires:	ruby
BuildRequires:	jpeg-devel
BuildRequires:	gomp-devel
BuildRequires:	pkgconfig(libspiro)
BuildRequires:	suitesparse-devel
BuildRequires:	pkgconfig(babl-0.1) >= 0.1.108
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4l1)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(lua)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(maxflow)
BuildRequires:	pkgconfig(OpenEXR) >= 3.1.0
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(poly2tri-c)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:  pkgconfig(jasper)
%description
GEGL (Generic Graphics Library) is a graph based image processing 
framework.

GEGLs original design was made to scratch GIMPs itches for a new 
compositing and processing core. This core is being designed to 
have minimal dependencies. and a simple well defined API. 

%package -n     %{libname}
Summary:	libgegl library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the libgegl shared library for %{name}.

%package -n     %{libsc}
Summary:	libgegl-sc library for %{name}
Group:		System/Libraries

%description -n	%{libsc}
This package contains the libgegl-sc shared library for %{name}.

%package -n     %{libnpd}
Summary:        libgegl-npd library for %{name}
Group:          System/Libraries

%description -n %{libnpd}
This package contains the libgegl-npd shared library for %{name}.

%package -n	%{devname}
Summary:	Header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libsc} = %{EVRD}
Requires:	%{libnpd} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the development files for %{name}.

%package -n	%{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n	%{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q 
%autopatch -p1

%build
# Needed or meson can't find math -lm
export LDFLAGS="%{optflags} -lm"
%meson -Dmrg=disabled
%meson_build

%install
%meson_install

%find_lang %{name}-%{api}

%files -f %{name}-%{api}.lang
%doc AUTHORS
%{_bindir}/*
%{_libdir}/gegl-%{api}/*.so
%{_libdir}/gegl-%{api}/*.json
%{_datadir}/vala/vapi/gegl-%{api}.deps
%{_datadir}/vala/vapi/gegl-%{api}.vapi
%{_datadir}/gegl-0.4/lua/*

%files -n %{libname}
%{_libdir}/libgegl-%{api}.so.%{major}*

%files -n %{libsc}
%{_libdir}/libgegl-sc-%{api}.so

%files -n %{libnpd}
%{_libdir}/libgegl-npd-%{api}.so

%files -n %{devname}
%doc
%{_libdir}/libgegl-%{api}.so
%{_includedir}/gegl-%{api}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-sc-%{api}.pc

%files -n %{girname}
%{_libdir}/girepository-1.0/Gegl-%{api}.typelib
%{_datadir}/gir-1.0/Gegl-%{api}.gir

%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1

%global optflags %{optflags} -O3

%define api 0.4
%define major 0
%define libname %mklibname %{name}
%define oldlibname %mklibname %{name} 0.4 0
%define libsc %mklibname %{name}-sc
%define oldlibsc %mklibname %{name}-sc 0.4
%define libnpd %mklibname %{name}-npd
%define oldlibnpd %mklibname %{name}-npd 0.4
%define devname %mklibname -d %{name}
%define olddevname %mklibname -d %{name} 0.4
%define	girname	%mklibname %{name}-gir
%define	oldgirname	%mklibname %{name}-gir 0.4

Summary:	GEGL (Generic Graphics Library) - graph based image processing framework
Name:		gegl
Version:	0.4.62
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
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libspiro)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4l1)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(lua)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(maxflow)
BuildRequires:	pkgconfig(OpenEXR) >= 3.1.0
BuildRequires:  pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(poly2tri-c)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:  pkgconfig(jasper)
BuildRequires:  python-gi
%description
GEGL (Generic Graphics Library) is a graph based image processing 
framework.

GEGLs original design was made to scratch GIMPs itches for a new 
compositing and processing core. This core is being designed to 
have minimal dependencies. and a simple well defined API. 

%package -n     %{libname}
Summary:	libgegl library for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description -n	%{libname}
This package contains the libgegl shared library for %{name}.

%package -n     %{libsc}
Summary:	libgegl-sc library for %{name}
Group:		System/Libraries
%rename %{oldlibsc}

%description -n	%{libsc}
This package contains the libgegl-sc shared library for %{name}.

%package -n     %{libnpd}
Summary:        libgegl-npd library for %{name}
Group:          System/Libraries
%rename %{oldlibnpd}

%description -n %{libnpd}
This package contains the libgegl-npd shared library for %{name}.

%package -n	%{devname}
Summary:	Header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libsc} = %{EVRD}
Requires:	%{libnpd} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
%rename %{olddevname}

%description -n	%{devname}
This package contains the development files for %{name}.

%package -n	%{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
%rename %{oldgirname}

%description -n	%{girname}
GObject Introspection interface description for %{name}.

%prep
%autosetup -p1

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
%doc %{_datadir}/doc/gegl-0.4/
%{_libdir}/libgegl-%{api}.so
%{_includedir}/gegl-%{api}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-sc-%{api}.pc

%files -n %{girname}
%{_libdir}/girepository-1.0/Gegl-%{api}.typelib
%{_datadir}/gir-1.0/Gegl-%{api}.gir

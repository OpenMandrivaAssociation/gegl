%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1

%define api 0.4
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libsc %mklibname %{name}-sc %{api}
%define libnpd %mklibname %{name}-npd %{api}
%define devname %mklibname -d %{name} %{api}

%define	girname	%mklibname %{name}-gir %{api}

Summary:	GEGL (Generic Graphics Library) - graph based image processing framework
Name:		gegl
Version:	0.4.4
#define	gitdate	
Release:	%{?gitdate:1.%{gitdate}.}1
Group:		System/Libraries
License:	LGPLv3+
Url:		http://www.gegl.org/
# git clone git://git.gnome.org/gegl
Source0:	http://download.gimp.org/pub/gegl/%{api}/%{name}-%{version}.tar.bz2
#Patch0:		gegl-0.3.28-ffmpeg-3.5.patch

BuildRequires:	enscript
BuildRequires:	intltool
BuildRequires:	graphviz
BuildRequires:	imagemagick
BuildRequires:	pango-modules
BuildRequires:	perl-devel
BuildRequires:	python-gobject-introspection
BuildRequires:	ruby
BuildRequires:	jpeg-devel
BuildRequires:	spiro-devel
BuildRequires:	suitesparse-devel
BuildRequires:	pkgconfig(babl) >= 0.1.52
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libopenraw-0.1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(poly2tri-c)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(vapigen)

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
%apply_patches

%build
export CC=gcc
export CXX=g++
%configure \
	--disable-workshop \
	--with-pango \
	--with-gdk-pixbuf \
	--disable-docs  \
	--with-pic \
	--with-cairo \
	--with-pangocairo \
	--with-lensfun \
	--with-libjpeg \
	--with-libpng \
	--with-librsvg \
	--with-openexr \
	--with-sdl \
	--with-libopenraw \
	--with-jasper \
	--with-graphviz \
	--with-lua \
	--with-libavformat \
	--with-libv4l2 \
	--without-libv4l \
	--with-libspiro \
	--with-exiv2 \
	--with-umfpack \
	--with-vala \
	--enable-introspection

%make

%install
%makeinstall_std
%find_lang %{name}-%{api}

%check
# temp disable
#make check

%files -f %{name}-%{api}.lang
%doc README AUTHORS NEWS
%{_bindir}/*
%{_libdir}/gegl-%{api}/*.so
%{_libdir}/gegl-%{api}/*.json
%{_datadir}/vala/vapi/gegl-%{api}.deps
%{_datadir}/vala/vapi/gegl-%{api}.vapi

%files -n %{libname}
%{_libdir}/libgegl-%{api}.so.%{major}*

%files -n %{libsc}
%{_libdir}/libgegl-sc-%{api}.so

%files -n %{libnpd}
%{_libdir}/libgegl-npd-%{api}.so

%files -n %{devname}
%doc ChangeLog
%{_libdir}/libgegl-%{api}.so
%{_includedir}/gegl-%{api}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-sc-%{api}.pc

%files -n %{girname}
%{_libdir}/girepository-1.0/Gegl-%{api}.typelib
%{_datadir}/gir-1.0/Gegl-%{api}.gir

%define	api	0.2
%define	major	0
%define	libname	%mklibname %{name} %{api}_%{major}
%define	devname	%mklibname -d %{name}

Summary:	GEGL (Generic Graphics Library) - graph based image processing framework
Name:		gegl
Version:	0.2.0
Release:	14
Group:		System/Libraries
License:	LGPLv3+
Url:		http://www.gegl.org/
Source0:	ftp://ftp.gimp.org/pub/gegl/%{api}/%{name}-%{version}.tar.bz2
Patch0:		gegl-0.2.0-ffmpeg-2.1.patch
Patch1:		gegl-0.2.0-lua-5.2.patch
Patch2:		gegl-0.2.0-CVE-2012-4433.patch
Patch3:		gegl-0.2.0-remove-src-over-op.patch
Patch4:		gegl-fix-introspection.patch

BuildRequires:	enscript
BuildRequires:	intltool
BuildRequires:	graphviz
BuildRequires:	imagemagick
BuildRequires:	pango-modules
BuildRequires:	perl-devel
BuildRequires:	ruby
#gw warning: this needs the deprecated libavcodec scaler (img_convert,...)
BuildRequires:	ffmpeg-devel
BuildRequires:	jpeg-devel
BuildRequires:	suitesparse-common-devel
BuildRequires:	pkgconfig(babl) >= 0.1.10
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libopenraw-1.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(sdl)

%description
GEGL (Generic Graphics Library) is a graph based image processing 
framework.

GEGLs original design was made to scratch GIMPs itches for a new 
compositing and processing core. This core is being designed to 
have minimal dependencies. and a simple well defined API. 

%package -n     %{libname}
Summary:	A library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains a shared library for %{name}.

%package -n	%{devname}
Summary:	Header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -q 
%apply_patches
sed -e 's/\.dylib/.bundle/' -i configure.ac || die
autoreconf -fi

%build
%configure2_5x \
	--enable-workshop \
	--with-pango \
	--with-gdk-pixbuf \
	--disable-docs  \
	--with-pic \
	--with-gio \
	--with-gtk \
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
	--with-libv4l \
	--with-libspiro \
	--with-exiv2 \
	--with-umfpack

%make

%install
%makeinstall_std
%find_lang %{name}-%{api}

%check
%make check

%files -f %{name}-%{api}.lang
%doc README AUTHORS NEWS
%{_bindir}/gegl
%{_libdir}/gegl-%{api}/*.so

%files -n %{libname}
%{_libdir}/libgegl-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_libdir}/*.so
%{_includedir}/gegl-%{api}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc


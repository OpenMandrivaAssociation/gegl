%define major 0
%define api 0.2
%define libname %mklibname %{name} %{api}_%{major}
%define develname %mklibname -d %{name}

Summary:	GEGL (Generic Graphics Library) - graph based image processing framework
Name:		gegl
Version:	0.2.0
Release:	4
Group:		System/Libraries
License:	LGPLv3+
URL:		http://www.gegl.org/
Source0:	ftp://ftp.gimp.org/pub/gegl/%{api}/%{name}-%{version}.tar.bz2
Patch0:		gegl-0.2.0-ffmpeg-0.11.patch

BuildRequires:	enscript
BuildRequires:	intltool
BuildRequires:	graphviz
BuildRequires:  imagemagick
BuildRequires:	pango-modules
BuildRequires:	ruby
#gw warning: this needs the deprecated libavcodec scaler (img_convert,...)
BuildRequires:	ffmpeg-devel
BuildRequires:	jpeg-devel
BuildRequires:  pkgconfig(babl) >= 0.1.10
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libopenraw-1.0)
BuildRequires:  pkgconfig(libpng15)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:	pkgconfig(sdl)

%description
GEGL (Generic Graphics Library) is a graph based image processing 
framework.

GEGLs original design was made to scratch GIMPs itches for a new 
compositing and processing core. This core is being designed to 
have minimal dependencies. and a simple well defined API. 

%package -n     %{libname}
Summary:        A library for %{name}
Group:          System/Libraries

%description -n %{libname}
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to
have minimal dependencies. and a simple well defined API.

%package -n     %{develname}
Summary:        Header files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to
have minimal dependencies. and a simple well defined API.

%prep
%setup -q 
%patch0 -p1 -b .ffmpeg11~
sed -i -e 's/\.dylib/.bundle/' configure.ac || die
autoreconf -fi

%build
%configure2_5x \
	--enable-workshop \
	--with-pango \
	--with-gdk-pixbuf \
	--without-libspiro \
	--disable-docs 
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc README AUTHORS NEWS
%{_bindir}/gegl
%{_libdir}/gegl-%{api}/*.so
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%files -n     %{libname}
%{_libdir}/libgegl-%{api}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/*.so
%{_includedir}/gegl-%{api}/
%{_libdir}/pkgconfig/%{name}-%{api}.pc


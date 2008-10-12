%define major 0
%define libname %mklibname %name %{major}
%define develname %mklibname -d %name

Name:		gegl
Version:	0.0.20
Release:	%mkrel 1
Summary:	GEGL (Generic Graphics Library) - graph based image processing framework
Group:		System/Libraries
License:	LGPLv3+
URL:		http://www.gegl.org/
Source0:	%{name}-%{version}.tar.bz2
Patch: gegl-0.0.20-new-ffmpeg.patch
Patch1: gegl-0.0.18-glib-build.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  babl-devel >= 0.0.22
BuildRequires:  glib2-devel
BuildRequires:  png-devel
BuildRequires:  pango-devel
BuildRequires:  ImageMagick
BuildRequires:	ruby
BuildRequires:	librsvg2-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	lua-devel
BuildRequires:	enscript
BuildRequires:	w3m
BuildRequires:	graphviz
BuildRequires:	gtk2-devel
BuildRequires:	SDL-devel
#gw warning: this needs the deprecated libavcodec scaler (img_convert,...)
BuildRequires:	ffmpeg-devel
BuildRequires:	jpeg-devel


%description
GEGL (Generic Graphics Library) is a graph based image processing 
framework.

GEGLs original design was made to scratch GIMPs itches for a new 
compositing and processing core. This core is being designed to 
have minimal dependencies. and a simple well defined API. 


%package -n     %{libname}
Summary:        A library for %name
Group:          System/Libraries

%description -n %{libname}
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to
have minimal dependencies. and a simple well defined API.

%package -n     %{develname}
Summary:        Header files for %name
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to
have minimal dependencies. and a simple well defined API.

%prep
%setup -q 
%patch -p1
%patch1 -p1
autoconf

%build

%configure2_5x --enable-workshop
%make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%_bindir/gegl

%files -n     %{libname}
%defattr(-,root,root)
%doc README AUTHORS NEWS
%_libdir/libgegl-0.0.so.%{major}*
%_libdir/gegl-0.0/


%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/%{name}
%_libdir/*.so
%_libdir/*.la
%_includedir/gegl-0.0/
%_libdir/pkgconfig/%{name}.pc


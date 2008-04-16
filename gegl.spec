%define major 0
%define libname %mklibname %name %{major}
%define develname %mklibname -d %name

Name:		gegl
Version:	0.0.16
Release:	%mkrel 1
Summary:	GEGL (Generic Graphics Library) - graph based image processing framework
Group:		System/Libraries
License:	GPL
URL:		http://www.gegl.org/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  babl-devel
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

%description
GEGL (Generic Graphics Library) is a graph based image processing 
framework.

GEGLs original design was made to scratch GIMPs itches for a new 
compositing and processing core. This core is being designed to 
have minimal dependencies. and a simple well defined API. 

%files
%defattr(-,root,root)
%_bindir/gegl

#--------------------------------------------------------------------

%package -n     %{libname}
Summary:        A library for %name
Group:          System/Libraries

%description -n %{libname}
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to
have minimal dependencies. and a simple well defined API.


%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n     %{libname}
%defattr(-,root,root)
%_libdir/libgegl-0.0.so.%{major}
%_libdir/libgegl-0.0.so.%{major}*
%_libdir/gegl-0.0/

#--------------------------------------------------------------------

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

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/%{name}
%_libdir/*.so
%_libdir/*.la
%_includedir/gegl-0.0/
%_libdir/pkgconfig/%{name}.pc
#--------------------------------------------------------------------

%prep

%setup -q 
%build

%configure --enable-workshop
%make

%install
%makeinstall

%clean
rm -fr %buildroot

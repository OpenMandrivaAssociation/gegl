%define major 0
%define libname %mklibname %name %{major}

Name:		gegl
Version:	0.0.12
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
%_libdir/libgegl-1.0.so.0
%_libdir/libgegl-1.0.so.0.%{major}.0

#--------------------------------------------------------------------

%package -n     %{libname}-devel
Summary:        Header files for %name
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to
have minimal dependencies. and a simple well defined API.

%files -n %{libname}-devel
%defattr(-,root,root)
%_libdir/gegl-1.0/*.so
%dir  %_includedir/gegl-1.0
%dir  %_includedir/gegl-1.0/%name
%_includedir/gegl-1.0/*.h
%_includedir/gegl-1.0/%name/*.h
%_libdir/pkgconfig/gegl.pc
%_libdir/libgegl-1.0.a
%_libdir/libgegl-1.0.la
%_libdir/libgegl-1.0.so
#--------------------------------------------------------------------

%prep

%setup -q 
%build

%configure
%make

%install
%makeinstall

%clean
rm -fr %buildroot

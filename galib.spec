Summary:	A C++ library of genetic algorithm components
Summary(pl.UTF-8):   Biblioteka C++ funkcji do algorytmów genetycznych
Name:		galib
Version:	246
Release:	1
License:	MIT (base library), GPL (GNU portions in examples)
Group:		Libraries
Source0:	http://lancet.mit.edu/ga/dist/%{name}%{version}.tgz
Patch0:		%{name}246_gcc4.patch
# Source0-md5:	e61efce22161907449b07f8472eb7c7c
URL:		http://lancet.mit.edu/ga/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAlib contains a set of C++ genetic algorithm objects. The library
includes tools for using genetic algorithms to do optimization in any
C++ program using any representation and genetic operators. The
documentation includes an extensive overview of how to implement a
genetic algorithm as well as examples illustrating customizations to
the GAlib classes.

%description -l pl.UTF-8
GAlib zawiera zbiór obiektów C++ do algorytmów genetycznych.
Biblioteka zawiera narzędzia do używania algorytmów genetycznych do
wykonywania optymalizacji w dowolnym programie C++ przy użyciu
dowolnej reprezentacji i operatorów genetycznych. Dokumentacja
zawiera obszerny opis sposobu implementacji algorytmu genetycznego, a
także przykłady ilustrujące dostosowanie klas GAliba do swoich
potrzeb.

%package devel
Summary:	Header files for GAlib
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki GAlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains header files for GAlib.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki GAlib.

%package static
Summary:	Static version of GAlib
Summary(pl.UTF-8):   Statyczna wersja biblioteki GAlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of GAlib.

%description static -l pl.UTF-8
Statyczna wersja biblioteki GAlib.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
%{__make} -C ga \
	CXX="libtool --mode=compile --tag CXX %{__cxx}" \
	CXXFLAGS="%{rpmcflags}" \
	LIB="libga.la" \
	AR="libtool --mode=link %{__cxx} %{rpmldflags} -rpath %{_libdir} -o libga.la \$(OBJS:.o=.lo) #"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install -C ga \
	LIB="libga.la" \
	INSTALL="libtool --mode=install install" \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README RELEASE-NOTES LICENSE
%attr(755,root,root) %{_libdir}/libga.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libga.so
%{_libdir}/libga.la
%{_includedir}/ga

%files static
%defattr(644,root,root,755)
%{_libdir}/libga.a

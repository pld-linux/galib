# TODO: build .so version of this library

Summary:	A C++ Library of Genetic Algorithm Components 
Name:		galib
Version:	245
Release:	1
License:	both MIT and GPL
Group:		Libraries
Source0:	ftp://lancet.mit.edu/pub/ga/%{name}%{version}.tar.gz
# Source0-md5:	5a19b7692c3c18741cc0a120d36de165
URL:		http://lancet.mit.edu/ga/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAlib contains a set of C++ genetic algorithm objects. The library includes
tools for using genetic algorithms to do optimization in any C++ program 
using any representation and genetic operators. The documentation includes 
an extensive overview of how to implement a genetic algorithm as well 
as examples illustrating customizations to the GAlib classes.

%package devel
Summary:	Header files for galib
Group:		Development/Libraries
%description devel
This package contains header files for galib

%prep
%setup -q -n %{name}%{version}

%build
cd ga
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}"
cd ..

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT/usr/lib

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT/usr

%clean
#rm -rf $RPM_BUILD_ROOT

#%%post
#/sbin/ldconfig

#%%postun
#/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README RELEASE-NOTES LICENSE
%attr(755,root,root) %{_libdir}/*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%dir %{_includedir}/ga
%{_includedir}/ga/*

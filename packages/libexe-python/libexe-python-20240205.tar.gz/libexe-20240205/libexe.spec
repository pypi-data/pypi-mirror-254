Name: libexe
Version: 20240205
Release: 1
Summary: Library to access the executable (EXE) format
Group: System Environment/Libraries
License: LGPL-3.0-or-later
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libexe
             
BuildRequires: gcc             

%description -n libexe
Library to access the executable (EXE) format

%package -n libexe-static
Summary: Library to access the executable (EXE) format
Group: Development/Libraries
Requires: libexe = %{version}-%{release}

%description -n libexe-static
Static library version of libexe.

%package -n libexe-devel
Summary: Header files and libraries for developing applications for libexe
Group: Development/Libraries
Requires: libexe = %{version}-%{release}

%description -n libexe-devel
Header files and libraries for developing applications for libexe.

%package -n libexe-python3
Summary: Python 3 bindings for libexe
Group: System Environment/Libraries
Requires: libexe = %{version}-%{release} python3
BuildRequires: python3-devel python3-setuptools

%description -n libexe-python3
Python 3 bindings for libexe

%package -n libexe-tools
Summary: Several tools for reading executable (EXE) files
Group: Applications/System
Requires: libexe = %{version}-%{release}

%description -n libexe-tools
Several tools for reading executable (EXE) files

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libexe
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so.*

%files -n libexe-static
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.a

%files -n libexe-devel
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/libexe.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libexe-python3
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.so

%files -n libexe-tools
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Feb  5 2024 Joachim Metz <joachim.metz@gmail.com> 20240205-1
- Auto-generated


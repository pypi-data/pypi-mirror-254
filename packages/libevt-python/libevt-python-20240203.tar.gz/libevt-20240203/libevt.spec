Name: libevt
Version: 20240203
Release: 1
Summary: Library to access the Windows Event Log (EVT) format
Group: System Environment/Libraries
License: LGPL-3.0-or-later
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libevt
                
BuildRequires: gcc                

%description -n libevt
Library to access the Windows Event Log (EVT) format

%package -n libevt-static
Summary: Library to access the Windows Event Log (EVT) format
Group: Development/Libraries
Requires: libevt = %{version}-%{release}

%description -n libevt-static
Static library version of libevt.

%package -n libevt-devel
Summary: Header files and libraries for developing applications for libevt
Group: Development/Libraries
Requires: libevt = %{version}-%{release}

%description -n libevt-devel
Header files and libraries for developing applications for libevt.

%package -n libevt-python3
Summary: Python 3 bindings for libevt
Group: System Environment/Libraries
Requires: libevt = %{version}-%{release} python3
BuildRequires: python3-devel python3-setuptools

%description -n libevt-python3
Python 3 bindings for libevt

%package -n libevt-tools
Summary: Several tools for reading Windows Event Log (EVT) files
Group: Applications/System
Requires: libevt = %{version}-%{release}     
     

%description -n libevt-tools
Several tools for reading Windows Event Log (EVT) files

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

%files -n libevt
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so.*

%files -n libevt-static
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.a

%files -n libevt-devel
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/libevt.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libevt-python3
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.so

%files -n libevt-tools
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Feb  3 2024 Joachim Metz <joachim.metz@gmail.com> 20240203-1
- Auto-generated


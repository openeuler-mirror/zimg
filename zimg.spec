Name:           zimg
Version:        3.0.3
Release:        1
Summary:        Scaling, color space conversion, and dithering library
License:        WTFPL
URL:            https://github.com/sekrit-twc/zimg

Source0:        %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake gcc-c++ libtool

%description
The "z" library implements the commonly required image processing basics of
scaling, color space conversion, and depth conversion. A simple API enables
conversion between any supported formats to operate with minimal knowledge from
the programmer. All library routines were designed from the ground-up with
correctness, flexibility, and thread-safety as first priorities. Allocation,
buffering, and I/O are cleanly separated from processing, allowing the
programmer to adapt "z" to many scenarios.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n zimg-release-%{version} -p0

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-testapp
%make_build V=1

%install
%make_install
install -m 755 -p -D testapp %{buildroot}%{_bindir}/testapp

find %{buildroot} -name '*.la' -delete

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md ChangeLog
%{_libdir}/lib%{name}.so.2.0.0
%{_libdir}/lib%{name}.so.2

%files devel
%{_bindir}/testapp
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Apr 14 2022 YukariChiba <i@0x7f.cc> - 3.0.3-1
- Upgrade version to 3.0.3

* Mon Aug 02 2021 linjiaxin5 <linjiaxin5@huawei.com> - 2.9.3-2
- Fix failure caused by GCC upgrade to 10

* Fri May 07 2021 weidong <weidong@uniontech.com> - 2.9.3-1
- Initial package.

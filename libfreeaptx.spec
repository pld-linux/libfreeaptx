Summary:	Open Source implementation of Audio Processing Technology codec (aptX)
Summary(pl.UTF-8):	Otwarta implementacja kodeka Audio Processing Technology (aptX)
Name:		libfreeaptx
Version:	0.2.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/iamthehorker/libfreeaptx/releases
Source0:	https://github.com/iamthehorker/libfreeaptx/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7e0f2ec62204cd808f2dd6b44800e554
URL:		https://github.com/iamthehorker/libfreeaptx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Open Source implementation of Audio Processing Technology
codec (aptX) derived from ffmpeg 4.0 project and licensed under LGPL
v2.1+. This codec is mainly used in Bluetooth A2DP profile.

%description -l pl.UTF-8
Ten pakiet zawiera mającą otwarte źródła implementację kodeka Audio
Processing Technology (aptX), wywodzącą się z projektu ffmpeg 4.0 i
udostępnioną na licencji LGPL w wersji 2.1+. Kodek jest używany
głównie w profilu Bluetooth A2DP.

%package devel
Summary:	Header files for freeaptx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki freeaptx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for freeaptx library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki freeaptx.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -W -Wall" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/freeaptxdec
%attr(755,root,root) %{_bindir}/freeaptxenc
%attr(755,root,root) %{_libdir}/libfreeaptx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfreeaptx.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreeaptx.so
%{_includedir}/freeaptx.h
%{_pkgconfigdir}/libfreeaptx.pc

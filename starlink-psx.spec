Summary:	PSX - POSIX interface routines
Summary(pl):	PSX - funkcje interfejsu POSIX
Name:		starlink-psx
Version:	0.4.218
Release:	1
License:	GPL
Group:		Libraries
#Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/psx/psx.tar.Z
Source0:	psx.tar.Z
# Source0-md5:	b83a11985632c67f3f351bf88860a134
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_PSX.html
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-ems-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
PSX is a FORTRAN subroutine library that allows programmers to use the
functionality provided by the POSIX and X/OPEN libraries. The use of
this library will enable programmers to make use of operating system
facilities in a machine independent way.

%description -l pl
PSX to biblioteka funkcji fortranowych pozwalaj±ca programistom
korzystaæ z funkcjonalno¶ci dostarczanej przez biblioteki POSIX i
X/OPEN. U¿ycie tej biblioteki umo¿liwia programistom korzystanie z
mo¿liwo¶ci systemu operacyjnego w sposób niezale¿ny od maszyny.

%package devel
Summary:	Header files for PSX library
Summary(pl):	Pliki nag³ówkowe biblioteki PSX
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	starlink-ems-devel

%description devel
Header files for PSX library.

%description devel -l pl
Pliki nag³ówkowe biblioteki PSX.

%package static
Summary:	Static Starlink PSX library
Summary(pl):	Statyczna biblioteka Starlink PSX
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Starlink PSX library.

%description static -l pl
Statyczna biblioteka Starlink PSX.

%prep
%setup -q -c

sed -i -e "s/ -O'/ %{rpmcflags} -fPIC'/;s/ ld -shared -soname / %{__cc} -shared \\\$\\\$3 -Wl,-soname=/" mk
sed -i -e "s/\\('-L\\\$(STAR_\\)LIB) /\\1SHARE) -lcnf /" makefile

%build
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc psx.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/psx_dev
%attr(755,root,root) %{stardir}/bin/psx_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a

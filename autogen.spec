%define	pre	pre4
Summary:	Automated program generator
Summary(pl.UTF-8):	Zautomatyzowany generator programów
Name:		autogen
Version:	5.13.0
Release:	0.%{pre}.1
License:	GPL v.2/BSD/LGPL
Group:		Development
Source0:	http://autogen.sourceforge.net/data/%{name}-%{version}%{pre}.tar.xz
# Source0-md5:	86f80b060d82ab1069043b3478df195f
URL:		http://autogen.sourceforge.net/
BuildRequires:	guile-devel
BuildRequires:	libltdl-devel
BuildRequires:	libxml2-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoGen is a tool designed for generating program files that contain
repetitive text with varied substitutions. Its goal is to simplify the
maintenance of programs that contain large amounts of repetitious
text. This is especially valuable if there are several blocks of such
text that must be kept synchronized in parallel tables.

%description -l pl.UTF-8
AutoGen to narzędzie zaprojektowane do generowania plików programów
zawierających powtarzający się tekst z różnymi podstawieniami. Celem
projektu jest uproszczenie zarządzania programów zawierających duże
ilości powtórzonego tekstu. Jest szczególnie wartościowy jeśli jest
kilka bloków takiego tekstu, które muszą być synchronizowane
równolegle.

%package devel
Summary:	Header files for autogen
Summary(pl.UTF-8):	Pliki nagłówkowe dla autogen
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for autogen.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla autogen.

%package static
Summary:	Static autogen library
Summary(pl.UTF-8):	Statyczna biblioteka autogen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static autogen library.

%description static -l pl.UTF-8
Statyczna biblioteka autogen.

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/pkgconfig/autoopts.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}
%{_infodir}/autogen.info*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/autoopts
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

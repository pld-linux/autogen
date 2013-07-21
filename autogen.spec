Summary:	Automated program generator
Summary(pl.UTF-8):	Zautomatyzowany generator programów
Name:		autogen
Version:	5.18
Release:	1
License:	GPL v3+ (AutoGen), LGPL v2+ (genshell), LGPL v3+ or Modified BSD (AutoOpts library)
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/autogen/rel%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	ef49893d65a490f4e1ae0a4d816cf6aa
Patch0:		%{name}-notinstalled.patch
Patch1:		%{name}-info.patch
URL:		http://autogen.sourceforge.net/
BuildRequires:	guile-devel
BuildRequires:	libltdl-devel
BuildRequires:	libxml2-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Suggests:	%{name}-devel = %{version}-%{release}
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

%package libs
Summary:	Shared AutoOpts library
Summary(pl.UTF-8):	Biblioteka współdzielona AutoOpts
License:	LGPL v3+ or Modified BSD
Group:		Libraries
Conflicts:	autogen < 5.14

%description libs
Shared AutoOpts library.

%description libs -l pl.UTF-8
Biblioteka współdzielona AutoOpts.

%package devel
Summary:	Header files for AutoOpts library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AutoOpts
License:	LGPL v3+ or Modified BSD
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for AutoOpts library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AutoOpts.

%package static
Summary:	Static AutoOpts library
Summary(pl.UTF-8):	Statyczna biblioteka AutoOpts
License:	LGPL v3+ or Modified BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AutoOpts library.

%description static -l pl.UTF-8
Statyczna biblioteka AutoOpts.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# .pc file is arch-dependent, so use arch-dependent pkgconfigdir
mv $RPM_BUILD_ROOT%{_datadir}/pkgconfig/autoopts.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/autogen
%attr(755,root,root) %{_bindir}/columns
%attr(755,root,root) %{_bindir}/getdefs
%attr(755,root,root) %{_bindir}/xml2ag
%{_datadir}/%{name}
%{_infodir}/autogen.info*
%{_mandir}/man1/autogen.1*
%{_mandir}/man1/columns.1*
%{_mandir}/man1/getdefs.1*
%{_mandir}/man1/xml2ag.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopts.so.25

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/autoopts-config
%attr(755,root,root) %{_libdir}/libopts.so
%{_libdir}/libopts.la
%{_includedir}/autoopts
%{_aclocaldir}/autoopts.m4
%{_pkgconfigdir}/autoopts.pc
%{_mandir}/man1/autoopts-config.1*
%{_mandir}/man3/ao_string_tokenize.3*
%{_mandir}/man3/configFileLoad.3*
%{_mandir}/man3/option*.3*
%{_mandir}/man3/str*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libopts.a

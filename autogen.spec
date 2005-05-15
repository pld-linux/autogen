Summary:	Automated program generator
Summary(pl):	Zautomatyzowany generator programów
Name:		autogen
Version:	5.7
Release:	1
License:	GPL v.2/BSD/LGPL
Group:		Development
Source0:	http://dl.sourceforge.net/autogen/%{name}-%{version}.tar.bz2
# Source0-md5:	7a90b2afac2de211f03c374e92dfe9b2
BuildRequires:	guile-devel
BuildRequires:	libxml2-devel
BuildRequires:	texinfo
URL:		http://autogen.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoGen is a tool designed for generating program files that contain
repetitive text with varied substitutions. Its goal is to simplify the
maintenance of programs that contain large amounts of repetitious
text. This is especially valuable if there are several blocks of such
text that must be kept synchronized in parallel tables.

#%description -l pl # write me

%package devel
Summary:	Header files for autogen
Summary(pl):	Pliki nagłówkowe dla autogen
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for autogen.

%description devel -l pl
Pliki nagłówkowe dla autogen.

%package static
Summary:	Static autogen library
Summary(pl):	Statyczna biblioteka autogen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static autogen library.

%description static -l pl
Statyczna biblioteka autogen.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_aclocaldir}/*.m4
%{_includedir}/autoopts
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

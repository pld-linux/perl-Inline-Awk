%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Awk
Summary:	Inline::Awk perl module
Summary(pl):	Modu³ perla Inline::Awk
Name:		perl-Inline-Awk
Version:	0.03
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	awk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Awk - Add awk code to your Perl programs.

%description -l pl
Modu³ Inline::Awk - pozwalaj±cy na u¿ywanie kodu awka w programach w
Perlu.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Inline/Awk.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

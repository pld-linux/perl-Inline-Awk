#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Awk
Summary:	Inline::Awk Perl module
Summary(cs):	Modul Inline::Awk pro Perl
Summary(da):	Perlmodul Inline::Awk
Summary(de):	Inline::Awk Perl Modul
Summary(es):	Módulo de Perl Inline::Awk
Summary(fr):	Module Perl Inline::Awk
Summary(it):	Modulo di Perl Inline::Awk
Summary(ja):	Inline::Awk Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Awk ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::Awk
Summary(pl):	Modu³ Perla Inline::Awk
Summary(pt):	Módulo de Perl Inline::Awk
Summary(pt_BR):	Módulo Perl Inline::Awk
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Awk
Summary(sv):	Inline::Awk Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Awk
Summary(zh_CN):	Inline::Awk Perl Ä£¿é
Name:		perl-Inline-Awk
Version:	0.03
Release:	3
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Inline
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

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
%{perl_vendorlib}/Inline/Awk.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*

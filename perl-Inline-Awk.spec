#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Awk
Summary:	Inline::Awk Perl module
Summary(cs.UTF-8):   Modul Inline::Awk pro Perl
Summary(da.UTF-8):   Perlmodul Inline::Awk
Summary(de.UTF-8):   Inline::Awk Perl Modul
Summary(es.UTF-8):   Módulo de Perl Inline::Awk
Summary(fr.UTF-8):   Module Perl Inline::Awk
Summary(it.UTF-8):   Modulo di Perl Inline::Awk
Summary(ja.UTF-8):   Inline::Awk Perl モジュール
Summary(ko.UTF-8):   Inline::Awk 펄 모줄
Summary(nb.UTF-8):   Perlmodul Inline::Awk
Summary(pl.UTF-8):   Moduł Perla Inline::Awk
Summary(pt.UTF-8):   Módulo de Perl Inline::Awk
Summary(pt_BR.UTF-8):   Módulo Perl Inline::Awk
Summary(ru.UTF-8):   Модуль для Perl Inline::Awk
Summary(sv.UTF-8):   Inline::Awk Perlmodul
Summary(uk.UTF-8):   Модуль для Perl Inline::Awk
Summary(zh_CN.UTF-8):   Inline::Awk Perl 模块
Name:		perl-Inline-Awk
Version:	0.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e98d19ea7b03b967c2aa4af872d11930
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	awk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Awk - Add awk code to your Perl programs.

%description -l pl.UTF-8
Moduł Inline::Awk - pozwalający na używanie kodu awka w programach w
Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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

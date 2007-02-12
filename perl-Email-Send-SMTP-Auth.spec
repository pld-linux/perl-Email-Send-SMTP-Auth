#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Send-SMTP-Auth
Summary:	Email::Send::SMTP::Auth - Send messages using SMTP with login/password
Summary(pl.UTF-8):   Email::Send::SMTP::Auth - wysyłanie wiadomości z użyciem autoryzacji SMTP
Name:		perl-Email-Send-SMTP-Auth
Version:	1.011
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f776a0af2956746f34b1b546382b11d2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Abstract
BuildRequires:	perl-Email-Send
BuildRequires:	perl-Net-SMTP_auth
BuildRequires:	perl-User
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This mailer for Email::Send uses Net::SMTP_auth to send a message via
an SMTP server, with basic authorization. The first invocation of send
requires three arguments after the message: the SMTP server name (or
IP address), login account name, and password. Subsequent calls will
remember these settings until/unless they are reset.

If your password is undef or empty-string, plain SMTP without
authorization will be used.

%description -l pl.UTF-8
To rozszerzenie Email::Send używa Net:::SMTP_auth do wysyłania
wiadomości poprzez serwer SMTP z użyciem autoryzacji. Pierwsze
wywołanie wymagana podania trzech argumentów poza wiadomością: nazwy
serwera SMTP (lub adresu IP), nazwy użytkownika oraz hasła. Późniejsze
wywołania będą korzystały z tych ustawień do czasu wyczyszczenia.

Jeśli jest niezdefiniowane lub puste, użyte będzie czyste SMTP bez
jakiejkolwiek autoryzacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Email/Send/SMTP/Auth.pm
%{_mandir}/man3/*

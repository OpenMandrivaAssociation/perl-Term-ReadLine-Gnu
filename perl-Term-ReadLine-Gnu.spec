%undefine _debugsource_packages
%define modname	Term-ReadLine-Gnu

Summary:	Perl extension for the GNU Readline/History Library 
Name:		perl-%{modname}
Version:	1.46
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Term/%{modname}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	pkgconfig(ncurses)

%description
This is an implementation of the interface to the GNU Readline
Library. This module gives you input line editing facility, input
history management facility, word completion facility, etc. It
uses the real GNU Readline Library. And this module has the
interface with the almost all variables and functions which are
documented in the GNU Readline/History Library. So you can program
your custom editing function, your custom completion function, and
so on with Perl. This may be useful for prototyping before
programming with C.

%prep
%autosetup -p1 -n %{modname}-%{version}
# Fix bogus dependency on /usr/local/bin/perl:
perl -pi -e 's!/usr/local/bin/perl!/usr/bin/perl!g' Gnu/{euc_jp,XS}.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make "CFLAGS=%{optflags}"

%check
if [ -n "$DISPLAY" ] ; then
	TERM=linux make test
else
	echo "***************************************************"
	echo " make test not done because DISPLAY var is not set "
	echo "***************************************************"
fi

%install
%makeinstall_std

%files
%{perl_vendorarch}/Term
%{perl_vendorarch}/auto/Term
%{_mandir}/man3/*
%{_bindir}/perlsh
%{_mandir}/man1/perlsh.1*




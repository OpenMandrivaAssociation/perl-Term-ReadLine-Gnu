%define module	Term-ReadLine-Gnu
%define name	perl-%{module}
%define version 1.19
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for the GNU Readline/History Library 
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Term/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
Obsoletes:	perl-Term-Readline-Gnu
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}
chmod 644 README
# Fix bogus dependency on /usr/local/bin/perl:
perl -pi -e 's!/usr/local/bin/perl!/usr/bin/perl!g' Gnu/{euc_jp,XS}.pm


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Term
%{perl_vendorarch}/auto/Term
%{_mandir}/*/*



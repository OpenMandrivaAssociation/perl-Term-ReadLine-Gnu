%define upstream_name	 Term-ReadLine-Gnu
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl extension for the GNU Readline/History Library 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	perl-devel
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes:	perl-Term-Readline-Gnu

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
%setup -q -n %{upstream_name}-%{upstream_version}
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

%define upstream_name	 Term-ReadLine-Gnu
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 8

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-7mdv2012.0
+ Revision: 765672
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-6
+ Revision: 764183
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-5
+ Revision: 667322
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.200.0-4mdv2011.0
+ Revision: 564584
- rebuild for perl 5.12.1

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 552641
- update to 1.20

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2010.1
+ Revision: 408084
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2010.0
+ Revision: 370184
- update to new version 1.19

* Sun Mar 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2009.1
+ Revision: 346266
- new version

* Wed Feb 25 2009 Thierry Vignaud <tv@mandriva.org> 1.17a-2mdv2009.1
+ Revision: 344792
- rebuild for new libreadline

* Fri Aug 29 2008 Olivier Thauvin <nanardon@mandriva.org> 1.17a-1mdv2009.0
+ Revision: 277158
- 1.17a

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.16-7mdv2009.0
+ Revision: 224122
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.16-6mdv2008.1
+ Revision: 151340
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.16-5mdv2008.0
+ Revision: 64782
- rebuild


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:15:16 (54145)
- rebuild

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:12:46 (54140)
Import perl-Term-ReadLine-Gnu

* Wed Apr 26 2006 Olivier Thauvin <nanardon@mandriva.org> 1.16-3mdk
- fix obsolete (-GNU != -Gnu)

* Thu Apr 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-2mdk
- fix duplication with perl-Term-Readline

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdk
- New release 1.16
- spec cleanup
- fix source URL
- better summary
- %%mkrel

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.15-1mdk
- 1.15

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.14-1mdk
- initial Mandriva package


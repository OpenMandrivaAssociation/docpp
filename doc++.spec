Summary:	A Documentation System for C, C++, IDL and Java
Name:		doc++
Version:	3.4.10
Release:	9
License:	GPLv2+
Group:		Publishing
URL:		http://docpp.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/docpp/doc++-%{version}.tar.bz2
Patch0:		gcc40_build_fix.patch
Patch1:		gcc41_build_fix.patch
Patch2:		segfault_fix.patch
Patch3:		translation_ja.patch
Patch4:		%{name}-3.4.10-fix-gcc43.patch
BuildRequires:	bison flex

%description
DOC++ is a documentation system for C, C++, IDL and Java, generating both TeX
output for high quality hardcopies and HTML output for sophisticated online
browsing of your documentation. The documentation is extracted directly from
the C/C++/IDL header/source files or Java class files.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .gcc43

%build

%configure2_5x

%make

%install
%makeinstall_std

# cleanup
rm -f %{buildroot}%{_datadir}/locale/locale.alias

%find_lang %{name}

%clean

%files -f %{name}.lang
%doc COPYING CREDITS NEWS PLATFORMS README REPORTING-BUGS doc/manual doc/doc++.conf 
%doc doc/docxx-br.sty doc/docxx-fr.sty doc/docxx-ja.sty doc/docxx-ro.sty doc/docxx.sty
%{_bindir}/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4.10-8mdv2011.0
+ Revision: 617866
- the mass rebuild of 2010.0 packages

* Wed Jun 10 2009 Jérôme Brenier <incubusss@mandriva.org> 3.4.10-7mdv2010.0
+ Revision: 384614
- add a patch to fix build with gcc43
- fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.4.10-4mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.4.10-4mdv2008.0
+ Revision: 89604
- rebuild

* Sat Jul 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3.4.10-3mdv2008.0
+ Revision: 49452
- added 4 patches from debian
- Import doc++



* Mon Jun 26 2006 Oden Eriksson <oeriksson@mandriva.com> 3.4.10-2mdv2007.0
- rebuild

* Sat May 21 2005 Oden Eriksson <oeriksson@mandriva.com> 3.4.10-1mdk
- initial Mandriva import

* Mon May 28 2001 Dragos Acostachioaie <dragos@iname.com>
    + took changes from Red Hat 7.1 Powertools

* Wed Dec 20 2000 Dragos Acostachioaie <dragos@iname.com>
    + added docxx-fr.sty, docxx-ro.sty
    + added french and romanian message files

* Sat Oct 14 2000 Dragos Acostachioaie <dragos@iname.com>
    + added docxx-br.sty

* Wed Jul 12 2000 Dragos Acostachioaie <dragos@iname.com>
    + added doc++.conf

* Sat Jul 08 2000 Dragos Acostachioaie <dragos@iname.com>
    + added russian messages files
    + added IDL to summaries and descriptions

* Sun Apr 16 2000 Dragos Acostachioaie <dragos@iname.com>
    + added REPORTING-BUGS

* Wed Dec  8 1999 Dragos Acostachioaie <dragos@iname.com>
    + added japanese messages file

* Fri Mar 19 1999 Dragos Acostachioaie <dragos@iname.com>
    + added french translation
      (provided by Marc Zonzon <Marc.Zonzon@univ-rennes1.fr>)
    + added spanish translation
      (provided by J. J. Merelo Guervos <jmerelo@kal-el.ugr.es>)

* Tue Mar 16 1999 Magnus Fromreide <magfr@lysator.liu.se>
    + added swedish translation

* Tue Mar 14 1999 Vitaly Fedrushkov <fedrushkov@acm.org>
    + Description in Russian

* Tue Mar  9 1999 Dragos Acostachioaie <dragos@iname.com>
    + relocatable RPM support
    + added `BuildRoot' clause

* Mon Mar  8 1999 Dragos Acostachioaie <dragos@iname.com>
    + change to install stripped binaries

* Tue Feb 16 1999 Dragos Acostachioaie <dragos@iname.com>
    + fixes to deal with the automake-generated Makefiles

* Thu Jan 21 1999 Dragos Acostachioaie <dragos@iname.com>
    + added doc/docxx.sty

* Sat Jan  2 1999 Dragos Acostachioaie <dragos@iname.com>
    + Final fixes for 3.3.5

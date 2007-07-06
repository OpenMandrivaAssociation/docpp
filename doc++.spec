Summary:	DOC++ - A Documentation System for C, C++, IDL and Java
Name:		doc++
Version:	3.4.10
Release:	%mkrel 2
License:	GPL
Group:		Publishing
URL:		http://docpp.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/docpp/doc++-%{version}.tar.bz2
BuildRequires:	bison flex
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
DOC++ is a documentation system for C, C++, IDL and Java,
generating both TeX output for high quality hardcopies and HTML
output for sophisticated online browsing of your documentation.
The documentation is extracted directly from the C/C++/IDL
header/source files or Java class files.

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_datadir}/locale/locale.alias

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING CREDITS NEWS PLATFORMS README REPORTING-BUGS doc/manual doc/doc++.conf 
%doc doc/docxx-br.sty doc/docxx-fr.sty doc/docxx-ja.sty doc/docxx-ro.sty doc/docxx.sty
%{_bindir}/*

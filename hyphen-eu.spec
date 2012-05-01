Name: hyphen-eu
Summary: Basque hyphenation rules
%define upstreamid 20080628
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
Source: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/hyph-eu.tex
Group: Applications/Text
URL: http://tp.lc.ehu.es/jma/basque.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-eu-cleantex.patch

%description
Basque hyphenation rules.

%prep
%setup -T -q -c -n hyphen-eu
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
grep -v "^%" hyph-eu.tex | tr ' ' '\n' > temp.tex
substrings.pl temp.tex hyph_eu_ES.dic ISO8859-1
echo "Created with substring.pl by substrings.pl hyph-eu.tex hyph_eu_ES.dic ISO8859-1" > README
echo "---" >> README
head -n 34 hyph-eu.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_eu_ES.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080628-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080628-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080628-1
- initial version

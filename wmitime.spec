Summary:	Standard and Internet Time clock applet
Summary(pl):	Zegar odmierzaj�cy standardowy oraz internetowy czas
Name:		wmitime
Version: 	0.3
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source:		http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
WMitime is an (overglorified) clock for the Windowmaker/Afterstep dock. 
It displays standard 12/24 hour time and date, as well as Swatch's new 
internet time.

%description -l pl
WMitime jest zegarem dla Doku WindowMakera/Afterstepa.
Wy�wietla standardowy 12/24 godzinny czas, dat�, jak 
r�wnie� nowy internetowy czas Swatcha.

%prep
%setup -q -n %{name}.app

%build

make -C %{name} \
	FLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf BUGS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Mon May 24 1999 Piotr Czerwi�ski <pius@pld.org.pl> 
  [0.3-1]
- updated to 0.3.

* Mon May 17 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [0.2-3]
- package is FHS 2.0 compliant,
- rewritten spec file for PLD use,
- based on spec by Jochem Wichers Hoeth <wiho@chem.uva.nl>.

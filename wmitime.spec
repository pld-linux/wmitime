Summary:	Standard and Internet Time clock applet
Summary(pl):	Zegar odmierzaj�cy standardowy oraz internetowy czas
Name:		wmitime
Version: 	0.2
Release:	3
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source:		http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix         /usr/X11R6

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
cd %{name}
make FLAGS="$RPM_OPT_FLAGS"

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
* Mon May 17 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [0.2-3]
- added using more rpm macros,
- package is FHS 2.0 compliant.

* Wed Apr  5 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [0.2-2]
- modified a bit spec file for PLD use.

* Fri Dec 18 1998 Jochem Wichers Hoeth <wiho@chem.uva.nl>
- first build.

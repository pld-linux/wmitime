Summary:	Standard and Internet Time clock applet
Summary(pl):	Zegar odmierzaj±cy standardowy oraz internetowy czas
Name:		wmitime
Version:	0.3
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.neotokyo.org/illusion/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMitime is an (overglorified) clock for the Windowmaker/Afterstep
dock. It displays standard 12/24 hour time and date, as well as
Swatch's new internet time.

%description -l pl
WMitime jest zegarem dla Doku WindowMakera/Afterstepa. Wy¶wietla
standardowy 12/24 godzinny czas, datê, jak równie¿ nowy internetowy
czas Swatcha.

%prep
%setup -q -n %{name}

%build
LANG=C; export LANG
%{__make} -C %{name} \
	FLAGS="%{rpmcflags} -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%attr(755,root,root) %{_bindir}/%{name}
#%%{_applnkdir}/DockApplets/wmitime.desktop

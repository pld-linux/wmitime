Summary: Standard and Internet Time clock applet
Name: wmitime
Version: 0.2
Release: 1
Copyright: GPL
Group: X11/Utilities
Source: http://www.neotokyo.org/illusion/wmitime-0.2.tar.gz
BuildRoot: /tmp/wmitime-root
Packager: Jochem Wichers Hoeth (wiho@chem.uva.nl)

%description
WMitime is an (overglorified) clock for the Windowmaker/Afterstep dock. It displays
standard 12/24 hour time and date, as well as Swatch's new internet time.

%changelog

%prep
%setup -n wmitime.app

%build
cd wmitime
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
cp wmitime/wmitime $RPM_BUILD_ROOT/usr/X11R6/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/X11R6/bin/wmitime
%doc BUGS
%doc CHANGES
%doc COPYING
%doc README

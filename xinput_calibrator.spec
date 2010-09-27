Summary: A generic touchscreen calibration program for X.Org
Name:    xinput_calibrator
Version: 0.7.0
Release: %mkrel 1
Source0: http://github.com/downloads/tias/xinput_calibrator/%{name}-%{version}.tar.gz
URL: http://www.freedesktop.org/wiki/Software/xinput_calibrator
License: MIT
Group:   System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtkmm2.4-devel

%description
xinput_calibrator is a program for calibrating your touchscreen, when using
the X Window System.
It currently features:
 - works for any standard Xorg touchscreen driver (uses XInput protocol)
 - mis-click detection (prevents bogus calibration)
 - dynamically recalibrates the evdev driver
 - outputs the calibration as xorg.conf.d snippet or HAL policy file
 - and more

%prep
%setup -q

%build
export CXXFLAGS="$RPM_OPT_FLAGS"
aclocal
autoconf
%configure --prefix=%{_prefix} --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
desktop-file-install                                    \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changelog README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1.*


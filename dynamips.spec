Summary: Cisco router simulator
Name: dynamips
Version: 0.2.15
Release: 1%{?dist}
License: GPLv2
Group: Applications/Emulators
URL: https://github.com/GNS3/%{name}

Source: https://github.com/GNS3/%{name}/archive/v%{version}.tar.gz

BuildRequires: cmake make
BuildRequires: glibc-devel
BuildRequires: libpcap-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: libuuid-devel

%description
This is a continuation of Dynamips, based on the last development version and improved
with patches wrote by various people from the community. This fork was named
Dynamips-community up to the 0.2.8-community release and renamed to the original Dynamips
on the 0.2.9 release.
You can compile two different versions of Dynamips with this code. Edit the Makefile to
set the flags to suit your environment. One of the flags, DYNAMIPS_CODE, can be "stable"
or "unstable".
Unstable is the code which contains most of the development code, and is in particular
suitable for use on a 64 bit Mac. Unfortunately this has proved to be unstable on other
platforms.
Stable contains the same code as Unstable, minus some mips64 bit optimisations and tcb
code which seems to trigger instability on a number of platforms. You should probably
use stable unless you have a very good reason.
For more information on the how to use Dynamips see the README file

%prep
%setup -n %{name}-%{version}
%cmake .

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%{_bindir}/dynamips
%{_bindir}/nvram_export
%doc %{_mandir}/man1/dynamips.1*
%doc %{_mandir}/man1/nvram_export.1*
%doc %{_mandir}/man7/hypervisor_mode.7*
%doc /usr/share/doc/dynamips/ChangeLog
%doc /usr/share/doc/dynamips/COPYING
%doc /usr/share/doc/dynamips/MAINTAINERS
%doc /usr/share/doc/dynamips/README
%doc /usr/share/doc/dynamips/README.hypervisor
%doc /usr/share/doc/dynamips/RELEASE-NOTES
%doc /usr/share/doc/dynamips/TODO

%changelog
* Wed May  27 2015 Dmitriy Slachshyov <dmnord@mital.kz> - 0.2.15-1
- Initial package.

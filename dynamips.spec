Summary: Cisco router simulator
Name: dynamips
Version: 0.2.15
Release: 3%{?dist}
License: GPLv2+
Group: Applications/Emulators
URL: https://github.com/GNS3/%{name}

Source: https://github.com/GNS3/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: glibc-devel
BuildRequires: libpcap-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: libuuid-devel

%description
This is a continuation of Dynamips, based on the last development version and
improved with patches wrote by various people from the community. This fork
was named Dynamips-community up to the 0.2.8-community release and renamed to
the original Dynamips on the 0.2.9 release.
You can compile two different versions of Dynamips with this code. Edit the
Makefile to set the flags to suit your environment. One of the flags,
DYNAMIPS_CODE, can be "stable" or "unstable".
Unstable is the code which contains most of the development code, and is in
particular suitable for use on a 64 bit Mac. Unfortunately this has proved to
be unstable on other platforms.
Stable contains the same code as Unstable, minus some mips64 bit optimisations
and tcb code which seems to trigger instability on a number of platforms. You
should probably use stable unless you have a very good reason.
For more information on the how to use Dynamips see the README file

%prep
%setup -q
rm -rf build && mkdir build

%build
pushd build
  %cmake ../
  make %{?_smp_mflags}
popd

%install
pushd build
  %make_install
popd
rm -rf %{buildroot}%{_datadir}/doc/%{name}/

%files
%license COPYING
%doc README.md README.hypervisor
%{_bindir}/dynamips
%{_bindir}/nvram_export
%{_mandir}/man1/dynamips.1.*
%{_mandir}/man1/nvram_export.1.*
%{_mandir}/man7/hypervisor_mode.7.*

%changelog
* Wed May  27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.15-2
- Clean spec

* Wed May  27 2015 Dmitriy Slachshyov <dmnord@mital.kz> - 0.2.15-1
- Initial package.

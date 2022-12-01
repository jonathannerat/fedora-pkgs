Name:           pamixer
Version:        1.6
Release:        2%{?dist}
Summary:        Pulseaudio command line mixer

License:        GPL-v3
URL:            https://github.com/cdemoulins/pamixer
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson cmake
BuildRequires:  g++
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  cxxopts-devel
Requires:       pulseaudio-libs
Requires:       cxxopts

%description
pamixer is like amixer but for pulseaudio. It can control the volume levels of the sinks.

Also, this project can provide you a small C++ library to control pulseaudio.

%prep
%autosetup

%build
%meson
%meson_build


%install
%meson_install


%files
%{_bindir}/pamixer
%{_mandir}/man1/pamixer.1.gz
%license COPYING


%changelog
* Thu Dec 01 2022 Jonathan Teran <jonathan.nerat@gmail.com> - 1.6-2
- Fix source tarball filename

* Thu Nov 24 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- Initial version of the package

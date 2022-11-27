Name:           cbatticon
Version:        1.6.13
Release:        1%{?dist}
Summary:        A lightweight and fast battery icon that sits in your system tray 

License:        GPLv2
URL:            https://github.com/valr/cbatticon
Source0:        https://github.com/valr/cbatticon/archive/refs/tags/1.6.13.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libnotify-devel

# VERBOSE=1 breaks the build
%define _make_verbose V=1

%description
%{summary}

%prep
%autosetup


%build
%make_build


%install
%make_install
%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/cbatticon
%{_mandir}/man1/cbatticon.1.gz
%{_docdir}/%{name}-%{version}/README


%changelog
* Sat Nov 26 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- Initial package version

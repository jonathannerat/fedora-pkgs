Name:           dragon
Version:        1.2.0
Release:        1%{?dist}
Summary:        Drag and drop source/target for X 

License:        GPLv3
URL:            https://github.com/mwh/dragon
Source0:        https://github.com/mwh/dragon/archive/refs/tags/v1.2.0.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel

%description
simple drag-and-drop source/sink for X or Wayland

%global debug_package %{nil}

%prep
%autosetup
sed -i 's:^PREFIX =.*:PREFIX=/usr:' Makefile


%build
%make_build


%install
%make_install


%files
%{_bindir}/dragon
%{_mandir}/man1/dragon.1.gz


%changelog
* Fri Nov 25 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- Initial package version

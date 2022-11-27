Name:           jonathannerat-dmenu
Version:        5.2.r17.g6f5aba7
Release:        1%{?dist}
Summary:        dmenu is an efficient dynamic menu for X.

License:        MIT
URL:            https://github.com/jonathannerat/dmenu
Source0:        jonathannerat-dmenu-5.2.r17.g6f5aba7.tar.gz

Provides:       dmenu = %{version}
Conflicts:      dmenu

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libXft-devel
# Requires:       

%description
%{summary}

%global debug_package %{nil}

%prep
%autosetup


%build
%make_build


%install
%make_install


%files
%doc README
%license LICENSE
%{_bindir}/dmenu
%{_bindir}/dmenu_path
%{_bindir}/dmenu_run
%{_bindir}/stest
%{_mandir}/man1/dmenu.1.gz
%{_mandir}/man1/stest.1.gz


%changelog
* Thu Nov 24 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- 

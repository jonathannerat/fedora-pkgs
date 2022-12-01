Name:           jonathannerat-dmenu
Version:        5.2.r19.ge582a0b
Release:        2%{?dist}
Summary:        dmenu is an efficient dynamic menu for X.

License:        MIT
URL:            https://github.com/jonathannerat/dmenu
Source0:        %{name}-%{version}.tar.gz

Provides:       dmenu = %{version}
Conflicts:      dmenu

BuildRequires:  gcc, make, libX11-devel, libXinerama-devel, fontconfig-devel, libXft-devel

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
* Thu Dec 01 2022 Jonathan Teran <jonathan.nerat@gmail.com> - 5.2.r19.ge582a0b-2
- Update package version, place BuildRequires in a single line

* Thu Nov 24 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- Initial package version

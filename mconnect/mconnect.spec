Name:           mconnect
Version:        v0.3.r55.g3991150
Release:        2%{?dist}
Summary:        mconnect - KDE Connect protocol implementation in Vala/C

License:        GPLv2
URL:            https://github.com/grimpy/mconnect
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  vala
BuildRequires:  meson
BuildRequires:  gdb
BuildRequires:  gnutls
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libgee-devel
BuildRequires:  json-glib-devel
BuildRequires:  gnutls-devel
BuildRequires:  libnotify-devel
BuildRequires:  gtk3-devel
BuildRequires:  at-spi2-core-devel
BuildRequires:  at-spi2-atk-devel

%description


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
install -D -m 644 extra/firewalld/mconnect.xml %{buildroot}%{_sysconfdir}/firewalld/services/mconnect.xml


%files
#license add-license-file-here
#doc add-docs-here
%{_bindir}/mconnect
%{_bindir}/mconnectctl
%{_datadir}/applications/mconnect.desktop
%{_datadir}/mconnect/mconnect.conf
%{_sysconfdir}/firewalld/services/mconnect.xml


%changelog
* Sat Nov 26 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- Initial package version
* Sat Nov 26 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- Add firewalld service file

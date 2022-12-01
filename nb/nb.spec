Name:           nb
Version:        7.1.2
Release:        1%{?dist}
Summary:        nb is a command line and local web note‑taking, bookmarking, archiving, and knowledge base application

License:        AGPLv3
URL:            https://github.com/xwmx/nb
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        Makefile

BuildRequires:  make
Requires:       bash, git
Recommends:     bat, nmap-ncat, pandoc, ripgrep, tig, w3m

%description
CLI and local web plain text note‑taking, bookmarking, and archiving with
linking, tagging, filtering, search, Git versioning & syncing, Pandoc
conversion, + more, in a single portable script. 

%prep
%autosetup
cp %{_sourcedir}/Makefile Makefile


%install
%make_install


%files
%{_bindir}/nb
%{_bindir}/bookmark


%changelog
* Thu Dec 01 2022 Jonathan Teran <jonathan.nerat@gmail.com>
- Initial package version

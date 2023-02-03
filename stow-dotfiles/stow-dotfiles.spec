Name:           stow-dotfiles
Version:        2.3.1
Release:        1%{?dist}
Summary:        Manage the installation of software packages from source

License:        GPLv3
URL:            https://www.gnu.org/software/stow/
Source0:        https://ftp.gnu.org/gnu/stow/stow-%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Fix --dotfiles option on directories
# https://github.com/aspiers/stow/issues/33#issuecomment-633255175
Patch0:         aitoratuin-dotfiles.patch

BuildRequires:  make perl-macros
BuildRequires:  perl(Test::More) perl(Test::Output)
Requires:       perl

Provides:       stow = %{version}
Provides:       perl(Stow) = %{version}
Provides:       perl(Stow::Util) = %{version}
Conflicts:      stow

%global debug_package %{nil}

%description
GNU Stow is a program for managing the installation of software packages,
keeping them separate (/usr/local/stow/emacs vs. /usr/local/stow/perl, for
example) while making them appear to be installed in the same place
(/usr/local). Software to ease the keeping track of software built from source,
making it easy to install, delete, move etc.


%prep
%setup -q -n stow-%{version}
%patch0 -p1


%build
%configure
%make_build


%install
%make_install


%files
%{_bindir}/stow
%{_bindir}/chkstow
%{_mandir}/man8/stow.8.*
%{_infodir}/stow.info.*
%{perl_privlib}/*
%license COPYING
%doc README.md
%exclude %{_docdir}/stow/*
%exclude %{_infodir}/dir


%changelog
* Fri Feb 03 2023 Jonathan Teran <jonathan.nerat@gmail.com>
- Initial package version

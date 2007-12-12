%define version 0.12
%define release 1mdk

Name:		sumika
Summary:  A dictionary management tool for Japanese translation engines
Version:        %{version}
Release:        %{release}
Group: 		System/Internationalization
License: GPL
URL: http://sourceforge.jp/projects/sumika/
Source0: %{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires: anthy uim
BuildRequires: gtk+2-devel libgdome-devel

%description
A dictionary management tool for anthy, canna, skk and prime.


%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove docs in %{_prefix}/doc/sumika/
rm -rf $RPM_BUILD_ROOT/%{_prefix}/doc/sumika/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING COPYING.canna ChangeLog
%doc README
%{_bindir}/sumika



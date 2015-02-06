%define		_class		System
%define		_subclass	ProcWatch
%define		upstream_name	%{_class}_%{_subclass}
%define __noautoreq /usr/bin/php

Name:		php-pear-%{upstream_name}
Version:	0.4.2
Release:	16
Summary:	Monitor processes

License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/System_ProcWatch/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
With this package you can monitor running processes based upon an XML
configuration file, XML string, INI file or an array where you define
patterns, conditions and actions.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/docs/*
%{_bindir}/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml





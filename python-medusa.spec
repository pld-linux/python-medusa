%define		module	medusa
Summary:	Framework for writing asynchronous socket-based servers
Summary(pl.UTF-8):	Szkielet do pisania asynchronicznych serwerów opartych na gniazdach
Name:		python-%{module}
Version:	0.5.4
Release:	7
License:	BSD-like (see LICENSE.txt)
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/m/medusa/%{module}-%{version}.tar.gz
# Source0-md5:	5d10505036bc38f8d4cb51d87516e069
URL:		http://www.amk.ca/python/code/medusa.html
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Medusa is an architecture for very-high-performance TCP/IP servers
(like HTTP, FTP, and SMTP). Medusa is different from most other
servers because it runs as a single process, multiplexing I/O with its
various client and server connections within a single process/thread.

%description -l pl.UTF-8
Medusa to architektura dla bardzo wysoko wydajnych serwerów TCP/IP
(jak HTTP, FTP czy SMTP). Medusa od większości innych serwerów różni
się tym, że działa jako pojedynczy proces, zwielokrotniający
wejście/wyjście na różne połączenia klientów i serwerów z poziomu
jednego procesu/wątku.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt TODO.txt CHANGES.txt LICENSE.txt docs
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

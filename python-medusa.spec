
%include	/usr/lib/rpm/macros.python
%define	pname	medusa

Summary:	Framework for writing asynchronous socket-based servers
Summary(pl):	Szkielet do pisania asynchronicznych serwerów opartych na gniazdach
Name:		python-%{pname}
Version:	0.5.4
Release:	1
License:	BSD-like (see LICENSE.txt)
Vendor:		Robin Dunn <robin@alldunn.com>
Group:		Development/Languages/Python
Source0:	http://www.amk.ca/files/python/%{pname}-%{version}.tar.gz
# Source0-md5:	5d10505036bc38f8d4cb51d87516e069
URL:		http://www.amk.ca/python/code/medusa.html
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Medusa is an architecture for very-high-performance TCP/IP servers
(like HTTP, FTP, and SMTP). Medusa is different from most other
servers because it runs as a single process, multiplexing I/O with its
various client and server connections within a single process/thread.

%description -l pl
Medusa to architektura dla bardzo wysoko wydajnych serwerów TCP/IP
(jak HTTP, FTP czy SMTP). Medusa od wiêkszo¶ci innych serwerów ró¿ni
siê tym, ¿e dzia³a jako pojedynczy proces, zwielokrotniaj±cy
wej¶cie/wyj¶cie na ró¿ne po³±czenia klientów i serwerów z poziomu
jednego procesu/w±tku.

%prep
%setup -q -n %{pname}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt TODO.txt CHANGES.txt LICENSE.txt docs
%{py_sitescriptdir}/%{pname}

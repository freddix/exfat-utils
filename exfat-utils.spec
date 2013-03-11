Summary:	Utilities for exFAT filesystem
Name:		exfat-utils
Version:	1.0.1
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: http://code.google.com/p/exfat/downloads/list
Source0:	http://exfat.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	e592130829d0bf61fa5e3cd1c759d329
URL:		http://code.google.com/p/exfat/
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to provide a full-featured exFAT file system
implementation for Linux and other Unix-like systems as a FUSE module.

%prep
%setup -q

%build
%scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%scons install \
	DESTDIR=$RPM_BUILD_ROOT%{_sbindir}

install dump/dumpexfat.8 fsck/exfatfsck.8 \
	label/exfatlabel.8 mkfs/mkexfatfs.8 \
	$RPM_BUILD_ROOT%{_mandir}/man8

echo '.so exfatfsck.8' >$RPM_BUILD_ROOT%{_mandir}/man8/fsck.exfat.8
echo '.so mkexfatfs.8' >$RPM_BUILD_ROOT%{_mandir}/man8/mkfs.exfat.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/dumpexfat
%attr(755,root,root) %{_sbindir}/exfatfsck
%attr(755,root,root) %{_sbindir}/exfatlabel
%attr(755,root,root) %{_sbindir}/fsck.exfat
%attr(755,root,root) %{_sbindir}/mkexfatfs
%attr(755,root,root) %{_sbindir}/mkfs.exfat
%{_mandir}/man8/*.8*


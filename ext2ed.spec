Summary:	An ext2 filesystem editor
Name:		ext2ed
Version:	0.1
Release:	%mkrel 35
License:	GPL+
Group:		System/Kernel and hardware 
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/filesystems/ext2/%{name}-%{version}.tar.bz2
Patch0:		ext2ed-0.1-config.patch
Patch1:		ext2ed-0.1-inode.patch
Patch2:		ext2ed-0.1-glibc.patch
Patch3:		ext2ed-0.1-compat21.patch
Patch4:		ext2ed-0.1-noreadline.patch
Patch5:		ext2ed-0.1-linux2.6-buildfix.patch
Patch6:		ext2ed-0.1-no-masix.patch
BuildRequires:	ncurses-devel readline-devel e2fsprogs-devel
# this should only be built on little endian machines!
ExclusiveArch:	alpha %{ix86} ppc x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ext2ed is a program which provides a text and window interface for
examining and editing an ext2 filesystem.  Ext2ed is supposed to be
easier to use than debugfs, but debugfs is more powerful.  Note that
this program should only be used by someone who is very experienced at
hacking filesystems.  

Install ext2ed if you want to examine and/or edit your ext2 filesystem,
and you know what you're doing.

%prep
%setup -q
%patch0 -p0 -b .config~
%patch1 -p1 -b .inode~
%patch2 -p1 -b .glibc~
%patch3 -p1 -b .compat21~
%patch4 -p1 -b .noreadline~
%patch5 -p1 -b .peroyvind~
%patch6 -p1 -b .no_masix~

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,%{_localstatedir}/lib}

make	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man8 \
	VAR_DIR=$RPM_BUILD_ROOT%{_localstatedir}/lib/ext2ed \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_localstatedir}/lib/ext2ed
%{_bindir}/ext2ed
%{_mandir}/man8/ext2ed.8*
%doc doc/user-guide-0.1.sgml
%doc doc/user-guide-0.1.ps
%doc doc/Ext2fs-overview-0.1.sgml


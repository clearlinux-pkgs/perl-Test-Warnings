#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Test-Warnings
Version  : 0.038
Release  : 62
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Warnings-0.038.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Warnings-0.038.tar.gz
Summary  : 'Test for warnings and the lack of them'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Warnings-license = %{version}-%{release}
Requires: perl-Test-Warnings-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Test-Warnings,
version 0.038:
Test for warnings and the lack of them

%package dev
Summary: dev components for the perl-Test-Warnings package.
Group: Development
Provides: perl-Test-Warnings-devel = %{version}-%{release}
Requires: perl-Test-Warnings = %{version}-%{release}

%description dev
dev components for the perl-Test-Warnings package.


%package license
Summary: license components for the perl-Test-Warnings package.
Group: Default

%description license
license components for the perl-Test-Warnings package.


%package perl
Summary: perl components for the perl-Test-Warnings package.
Group: Default
Requires: perl-Test-Warnings = %{version}-%{release}

%description perl
perl components for the perl-Test-Warnings package.


%prep
%setup -q -n Test-Warnings-0.038
cd %{_builddir}/Test-Warnings-0.038
pushd ..
cp -a Test-Warnings-0.038 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Warnings
cp %{_builddir}/Test-Warnings-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-Test-Warnings/7172e25a8f4dedd2d3425c7c01347f76166e018d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test2::Warnings.3
/usr/share/man/man3/Test::Warnings.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Warnings/7172e25a8f4dedd2d3425c7c01347f76166e018d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

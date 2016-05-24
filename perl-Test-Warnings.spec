#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Warnings
Version  : 0.026
Release  : 12
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Test-Warnings-0.026.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Test-Warnings-0.026.tar.gz
Summary  : 'Test for warnings and the lack of them'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Warnings-doc

%description
This archive contains the distribution Test-Warnings,
version 0.026:
Test for warnings and the lack of them

%package doc
Summary: doc components for the perl-Test-Warnings package.
Group: Documentation

%description doc
doc components for the perl-Test-Warnings package.


%prep
%setup -q -n Test-Warnings-0.026

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/Test/Warnings.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

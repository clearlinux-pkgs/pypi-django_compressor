#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-django_compressor
Version  : 3.1
Release  : 57
URL      : https://files.pythonhosted.org/packages/ef/3d/6580ac89d2677e77893b9a977938d833d3894ca8cc3161b5422d0d00386b/django_compressor-3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/3d/6580ac89d2677e77893b9a977938d833d3894ca8cc3161b5422d0d00386b/django_compressor-3.1.tar.gz
Summary  : Compresses linked and inline JavaScript or CSS into single cached files.
Group    : Development/Tools
License  : MIT NCSA
Requires: pypi-django_compressor-license = %{version}-%{release}
Requires: pypi-django_compressor-python = %{version}-%{release}
Requires: pypi-django_compressor-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: django_compressor
Provides: django_compressor-python
Provides: django_compressor-python3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(django_appconf)
BuildRequires : pypi(rcssmin)
BuildRequires : pypi(rjsmin)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
Django Compressor
=================
.. image:: https://codecov.io/github/django-compressor/django-compressor/coverage.svg?branch=develop
:target: https://codecov.io/github/django-compressor/django-compressor?branch=develop

%package license
Summary: license components for the pypi-django_compressor package.
Group: Default

%description license
license components for the pypi-django_compressor package.


%package python
Summary: python components for the pypi-django_compressor package.
Group: Default
Requires: pypi-django_compressor-python3 = %{version}-%{release}

%description python
python components for the pypi-django_compressor package.


%package python3
Summary: python3 components for the pypi-django_compressor package.
Group: Default
Requires: python3-core
Provides: pypi(django_compressor)
Requires: pypi(django_appconf)
Requires: pypi(rcssmin)
Requires: pypi(rjsmin)

%description python3
python3 components for the pypi-django_compressor package.


%prep
%setup -q -n django_compressor-3.1
cd %{_builddir}/django_compressor-3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641432828
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . rjsmin
pypi-dep-fix.py . rcssmin
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-django_compressor
cp %{_builddir}/django_compressor-3.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-django_compressor/56d7505d0f3261ee8a924a2e8841242e027126fb
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} rjsmin
pypi-dep-fix.py %{buildroot} rcssmin
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-django_compressor/56d7505d0f3261ee8a924a2e8841242e027126fb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

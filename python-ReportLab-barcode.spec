Summary:	The barcode extension for ReportLab
Name:		python-ReportLab-barcode
Version:	0.9.2
Release:	5
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.com/ftp/extensions/rlbarcode-%{version}.tgz
# Source0-md5:	eb116d682abf5aa55683da90d6eca76f
URL:		http://www.reportlab.com/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
Requires:	python-ReportLab
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This barcode extension for ReportLab support code39, code93 and
code128 barcode formats.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/reportlab/extensions/barcode

cp -a reportlab/extensions/barcode/*.py $RPM_BUILD_ROOT%{py_sitescriptdir}/reportlab/extensions/barcode

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/reportlab/extensions
%dir %{py_sitescriptdir}/reportlab/extensions/barcode
%{py_sitescriptdir}/reportlab/extensions/barcode/*.py[co]

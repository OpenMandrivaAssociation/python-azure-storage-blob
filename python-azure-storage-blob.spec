%define module azure-storage-blob
%define oname azure_storage_blob

Name:		python-azure-storage-blob
Version:	12.29.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Microsoft Azure Blob Storage Client Library for Python
URL:		https://pypi.org/project/azure-storage-blob/
License:	MIT License
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Microsoft Azure Blob Storage Client Library for Python

%files
%{py_sitedir}/azure
%{py_sitedir}/%{oname}-%{version}.dist-info

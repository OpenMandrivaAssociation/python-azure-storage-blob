Name:		python-azure-storage-blob
Version:	12.24.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/azure-storage-blob/azure_storage_blob-%{version}.tar.gz
Summary:	Microsoft Azure Blob Storage Client Library for Python
URL:		https://pypi.org/project/azure-storage-blob/
License:	MIT License
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Microsoft Azure Blob Storage Client Library for Python

%prep
%autosetup -p1 -n azure_storage_blob-%{version}

%files
%{py_sitedir}/azure
%{py_sitedir}/azure_storage_blob-*.*-info

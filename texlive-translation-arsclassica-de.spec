%global tl_name translation-arsclassica-de
%global tl_revision 23803

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	German version of arsclassica
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/arsclassica/de
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-arsclassica-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-arsclassica-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a "translation" of the arsclassica documentation.


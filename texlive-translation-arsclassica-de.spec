Name:		texlive-translation-arsclassica-de
Version:	23803
Release:	1
Summary:	German version of arsclassica
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/arsclassica/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-arsclassica-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-arsclassica-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the arsclassica dcoumentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-arsclassica-de/ArsClassica-de.pdf
%doc %{_texmfdistdir}/doc/latex/translation-arsclassica-de/ArsClassica-de.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

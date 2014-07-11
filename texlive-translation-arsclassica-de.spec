# revision 23803
# category Package
# catalog-ctan /info/translations/arsclassica/de
# catalog-date 2011-09-01 19:45:17 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-arsclassica-de
Version:	20110901
Release:	8
Summary:	German version of arsclassica
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/arsclassica/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-arsclassica-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-arsclassica-de.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110901-2
+ Revision: 757078
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110901-1
+ Revision: 719793
- texlive-translation-arsclassica-de
- texlive-translation-arsclassica-de
- texlive-translation-arsclassica-de


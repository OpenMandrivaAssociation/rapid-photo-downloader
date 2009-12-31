%define name	rapid-photo-downloader
%define version	0.1.0
%define prever beta2
%define release	%mkrel 1
%define Summary	Images downloader for external devices
%define _iconstheme    hicolor
%define _icons16dir    %_iconsdir/%{_iconstheme}/16x16/apps
%define _icons22dir    %_iconsdir/%{_iconstheme}/22x22/apps
%define _icons24dir    %_iconsdir/%{_iconstheme}/24x24/apps
%define _icons48dir    %_iconsdir/%{_iconstheme}/48x48/apps


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/rapid/trunk/%{version}/+download/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Graphics
URL:		http://damonlynch.net/rapid
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel >= 2.5
BuildRequires:	desktop-file-utils
Requires:	findutils
Requires:	python-imaging
Requires:	gtk2
Requires:	pygtk2
Requires:	python-exiv2
Requires:	hicolor-icon-theme
Requires:	gnome-python-gconf
Suggests:	librsvg2

%description
Rapid Photo Downloader is written by a photographer for professional
and amateur photographers. Released under the GNU GPL license, it is
designed for use on the Linux Desktop. It can download photos from
multiple cameras, memory cards, and Portable Storage Devices
simultaneously. It provides many options for subfolder
creation, image renaming and backup.

%files  -f %{name}.lang
%defattr(-,root,root)
%doc rapid/AUTHORS rapid/ChangeLog rapid/COPYING rapid/TODO rapid/INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%_icons16dir/%{name}.png
%_icons22dir/%{name}.png
%_icons24dir/%{name}.png
%_icons48dir/%{name}.png
%_datadir/pixmaps/%{name}.png
%_datadir/pixmaps/%{name}.xpm
%{py_puresitedir}/rapid/
%{py_puresitedir}/*.egg-info

#---------------------------------------------------------------------

%prep
%setup -q 

%build


%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

chmod 755 %{buildroot}/%{py_puresitedir}/rapid/renamesubfolderprefs.py \
%{buildroot}/%{py_puresitedir}/rapid/common.py %{buildroot}/%{py_puresitedir}/rapid/metadata.py \
%{buildroot}/%{py_puresitedir}/rapid/media.py %{buildroot}/%{py_puresitedir}/rapid/tableplusminus.py \
%{buildroot}/%{py_puresitedir}/rapid/misc.py %{buildroot}/%{py_puresitedir}/rapid/rapid.py \
%{buildroot}/%{py_puresitedir}/rapid/renamesubfolderprefstest.py

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

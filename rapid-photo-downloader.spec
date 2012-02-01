Name:		rapid-photo-downloader
Version:	0.4.3
Release:	%mkrel 1
Summary:	Images downloader for external devices
License:	GPLv2
Group:		Graphics
URL:		http://damonlynch.net/rapid
Source0:	http://launchpad.net/rapid/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	desktop-file-utils
Requires:	findutils
Requires:	python-imaging
Requires:	python-kaa-metadata
Requires:	python-hachoir-metadata
Requires:	gtk2
Requires:	pygtk2
# Do NOT backport it to 2010.1 as python-exiv2 is too old there and
# cannot be backported due to python >= 2.7 requires
Requires:	python-exiv2 >= 0.3.0
Requires:	exiv2
Requires:	hicolor-icon-theme
Requires:	gnome-python-gconf
Requires:	ffmpegthumbnailer
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
%doc rapid/AUTHORS rapid/ChangeLog rapid/COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{py_puresitedir}/rapid/
%{py_puresitedir}/*.egg-info

#---------------------------------------------------------------------

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

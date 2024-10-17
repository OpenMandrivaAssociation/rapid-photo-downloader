Name:		rapid-photo-downloader
Version:	0.4.5
Release:	2
Summary:	Images downloader for external devices
License:	GPLv2
Group:		Graphics
URL:		https://damonlynch.net/rapid
Source0:	https://launchpad.net/rapid/trunk/0.4.5/+download/%{name}-%{version}.tar.gz
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


%changelog
* Wed Feb 01 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.3-1mdv2011.0
+ Revision: 770374
- New version 0.4.3, update BuildRequires, spec cleanup

* Sun Jan 02 2011 John Balcaen <mikala@mandriva.org> 0.3.4-1mdv2011.0
+ Revision: 627500
- Update to 0.3.4

  + Sandro Cazzaniga <kharec@mandriva.org>
    - new version 0.3.3

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 0.3.1-2mdv2011.0
+ Revision: 599637
- rebuild for py2.7

* Sun Sep 05 2010 John Balcaen <mikala@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 576191
- Update to 0.3.1

* Sun Jul 25 2010 John Balcaen <mikala@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 559877
- Update to 0.3.0
- add somes requires suggested by upstream

* Wed Feb 17 2010 John Balcaen <mikala@mandriva.org> 0.1.3-1mdv2010.1
+ Revision: 506891
- update to 0.1.3

* Sun Jan 17 2010 John Balcaen <mikala@mandriva.org> 0.1.2-1mdv2010.1
+ Revision: 492629
- Update to 0.1.2

* Thu Jan 07 2010 Frederik Himpe <fhimpe@mandriva.org> 0.1.1-1mdv2010.1
+ Revision: 487289
- update to new version 0.1.1

* Thu Dec 31 2009 John Balcaen <mikala@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 484310
- Update to 0.1.0

* Fri Dec 04 2009 John Balcaen <mikala@mandriva.org> 0.1.0-0.beta2mdv2010.1
+ Revision: 473232
- Update to 0.1.0beta2

* Sat Sep 26 2009 John Balcaen <mikala@mandriva.org> 0.0.10-1mdv2010.0
+ Revision: 449395
- import rapid-photo-downloader



Name:		netrek-client-cow
Version:	3.3.1
Release:	4
Summary:	Netrek client
License:	MIT
Group:		Games/Other
Source0:	http://netrek.org/files/COW/%{name}-%{version}.tar.gz
Source1:	%{name}.6
URL:		http://www.netrek.org/

BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel
BuildRequires:	imlib2-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	gmp-devel

%description
This is a client for the multiplayer game of Netrek, supporting sound,
color bitmaps, and recording and playback of games. The game itself has 
existed since 1988, and had a solid player-base, including some 
people who have been playing for nearly as long as the game has existed.


%prep
%setup -q

%build
%configure
#Package doesn't support concurrent makes yet. forcing "-j1"
make -j1

%install
%makeinstall
#Dont set execute on .desktop file
chmod -x %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -m 0644 %{SOURCE1} -D %{buildroot}/%{_mandir}/man6/%{name}.6

%files
# "COPYING" is a list of authors, and not the GPL license
%doc CHANGES README.* TODO *.DOC COPYING XTREKRC.example copyright*.h
%doc cow.html index.orig.html newbie.html cow.css stars.gif netrekrc.example
%{_gamesbindir}/%{name}
%{_datadir}/pixmaps/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/*.6*


%changelog
* Sat Mar 03 2012 Johnny A. Solbu <solbu@mandriva.org> 3.3.1-3
+ Revision: 781984
- Adding manfile, from Debian
- Spec cleanup

* Thu Mar 01 2012 Johnny A. Solbu <solbu@mandriva.org> 3.3.1-2
+ Revision: 781479
- Package doesn't support concurrent builds.
- Remove execute perm on desktop file
- import netrek-client-cow


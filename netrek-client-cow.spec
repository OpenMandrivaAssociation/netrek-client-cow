%define subrel 1

Name:		netrek-client-cow
Version:	3.3.1
Release:	1
Summary:	Netrek client
License:	MIT
Group:		Games/Other
Source0:	http://netrek.org/files/COW/%{name}-%{version}.tar.gz
URL:		http://www.netrek.org

BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel
BuildRequires:	imlib2-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	gmp-devel

%description
This is a client for the multiplayer game of Netrek, supporting sound,
color bitmaps recording and playback of games. The game itself has 
existed for over 20 years, and has a solid playerbase, including some 
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

%files
# "COPYING" is a list of authors, and not the GPL license
%doc CHANGES README.* TODO *.DOC COPYING XTREKRC.example copyright*.h
%doc cow.html index.orig.html newbie.html cow.css stars.gif netrekrc.example
%{_gamesbindir}/%{name}
%{_datadir}/pixmaps/%{name}/*
%{_datadir}/applications/%{name}.desktop

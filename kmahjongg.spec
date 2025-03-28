#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmahjongg
Version  : 24.12.3
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.12.3/src/kmahjongg-24.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.3/src/kmahjongg-24.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.3/src/kmahjongg-24.12.3.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kmahjongg-bin = %{version}-%{release}
Requires: kmahjongg-data = %{version}-%{release}
Requires: kmahjongg-license = %{version}-%{release}
Requires: kmahjongg-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : libkmahjongg-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
MINIMAL

%package bin
Summary: bin components for the kmahjongg package.
Group: Binaries
Requires: kmahjongg-data = %{version}-%{release}
Requires: kmahjongg-license = %{version}-%{release}

%description bin
bin components for the kmahjongg package.


%package data
Summary: data components for the kmahjongg package.
Group: Data

%description data
data components for the kmahjongg package.


%package doc
Summary: doc components for the kmahjongg package.
Group: Documentation

%description doc
doc components for the kmahjongg package.


%package license
Summary: license components for the kmahjongg package.
Group: Default

%description license
license components for the kmahjongg package.


%package locales
Summary: locales components for the kmahjongg package.
Group: Default

%description locales
locales components for the kmahjongg package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kmahjongg-24.12.3
cd %{_builddir}/kmahjongg-24.12.3
pushd ..
cp -a kmahjongg-24.12.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742461391
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742461391
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmahjongg
cp %{_builddir}/kmahjongg-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmahjongg/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kmahjongg-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmahjongg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmahjongg-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmahjongg/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmahjongg-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kmahjongg/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kmahjongg-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kmahjongg
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kmahjongg
/usr/bin/kmahjongg

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmahjongg.desktop
/usr/share/config.kcfg/kmahjongg.kcfg
/usr/share/icons/hicolor/128x128/apps/kmahjongg.png
/usr/share/icons/hicolor/16x16/apps/kmahjongg.png
/usr/share/icons/hicolor/22x22/apps/kmahjongg.png
/usr/share/icons/hicolor/32x32/apps/kmahjongg.png
/usr/share/icons/hicolor/48x48/apps/kmahjongg.png
/usr/share/icons/hicolor/64x64/apps/kmahjongg.png
/usr/share/icons/hicolor/scalable/apps/kmahjongg.svgz
/usr/share/kmahjongg/layouts/4_winds.desktop
/usr/share/kmahjongg/layouts/4_winds.layout
/usr/share/kmahjongg/layouts/Vi.desktop
/usr/share/kmahjongg/layouts/Vi.layout
/usr/share/kmahjongg/layouts/X_shaped.desktop
/usr/share/kmahjongg/layouts/X_shaped.layout
/usr/share/kmahjongg/layouts/alien.desktop
/usr/share/kmahjongg/layouts/alien.layout
/usr/share/kmahjongg/layouts/altar.desktop
/usr/share/kmahjongg/layouts/altar.layout
/usr/share/kmahjongg/layouts/arena.desktop
/usr/share/kmahjongg/layouts/arena.layout
/usr/share/kmahjongg/layouts/arrow.desktop
/usr/share/kmahjongg/layouts/arrow.layout
/usr/share/kmahjongg/layouts/atlantis.desktop
/usr/share/kmahjongg/layouts/atlantis.layout
/usr/share/kmahjongg/layouts/aztec.desktop
/usr/share/kmahjongg/layouts/aztec.layout
/usr/share/kmahjongg/layouts/balance.desktop
/usr/share/kmahjongg/layouts/balance.layout
/usr/share/kmahjongg/layouts/bat.desktop
/usr/share/kmahjongg/layouts/bat.layout
/usr/share/kmahjongg/layouts/bug.desktop
/usr/share/kmahjongg/layouts/bug.layout
/usr/share/kmahjongg/layouts/castle.desktop
/usr/share/kmahjongg/layouts/castle.layout
/usr/share/kmahjongg/layouts/castle2.desktop
/usr/share/kmahjongg/layouts/castle2.layout
/usr/share/kmahjongg/layouts/cat.desktop
/usr/share/kmahjongg/layouts/cat.layout
/usr/share/kmahjongg/layouts/chains.desktop
/usr/share/kmahjongg/layouts/chains.layout
/usr/share/kmahjongg/layouts/checkered.desktop
/usr/share/kmahjongg/layouts/checkered.layout
/usr/share/kmahjongg/layouts/chip.desktop
/usr/share/kmahjongg/layouts/chip.layout
/usr/share/kmahjongg/layouts/clubs.desktop
/usr/share/kmahjongg/layouts/clubs.layout
/usr/share/kmahjongg/layouts/columns.desktop
/usr/share/kmahjongg/layouts/columns.layout
/usr/share/kmahjongg/layouts/crab.desktop
/usr/share/kmahjongg/layouts/crab.layout
/usr/share/kmahjongg/layouts/cross.desktop
/usr/share/kmahjongg/layouts/cross.layout
/usr/share/kmahjongg/layouts/default.desktop
/usr/share/kmahjongg/layouts/default.layout
/usr/share/kmahjongg/layouts/dragon.desktop
/usr/share/kmahjongg/layouts/dragon.layout
/usr/share/kmahjongg/layouts/eagle.desktop
/usr/share/kmahjongg/layouts/eagle.layout
/usr/share/kmahjongg/layouts/enterprise.desktop
/usr/share/kmahjongg/layouts/enterprise.layout
/usr/share/kmahjongg/layouts/explosion.desktop
/usr/share/kmahjongg/layouts/explosion.layout
/usr/share/kmahjongg/layouts/flowers.desktop
/usr/share/kmahjongg/layouts/flowers.layout
/usr/share/kmahjongg/layouts/future.desktop
/usr/share/kmahjongg/layouts/future.layout
/usr/share/kmahjongg/layouts/galaxy.desktop
/usr/share/kmahjongg/layouts/galaxy.layout
/usr/share/kmahjongg/layouts/garden.desktop
/usr/share/kmahjongg/layouts/garden.layout
/usr/share/kmahjongg/layouts/girl.desktop
/usr/share/kmahjongg/layouts/girl.layout
/usr/share/kmahjongg/layouts/glade.desktop
/usr/share/kmahjongg/layouts/glade.layout
/usr/share/kmahjongg/layouts/grid.desktop
/usr/share/kmahjongg/layouts/grid.layout
/usr/share/kmahjongg/layouts/helios.desktop
/usr/share/kmahjongg/layouts/helios.layout
/usr/share/kmahjongg/layouts/hole.desktop
/usr/share/kmahjongg/layouts/hole.layout
/usr/share/kmahjongg/layouts/inner_circle.desktop
/usr/share/kmahjongg/layouts/inner_circle.layout
/usr/share/kmahjongg/layouts/key.desktop
/usr/share/kmahjongg/layouts/key.layout
/usr/share/kmahjongg/layouts/km.desktop
/usr/share/kmahjongg/layouts/km.layout
/usr/share/kmahjongg/layouts/labyrinth.desktop
/usr/share/kmahjongg/layouts/labyrinth.layout
/usr/share/kmahjongg/layouts/mask.desktop
/usr/share/kmahjongg/layouts/mask.layout
/usr/share/kmahjongg/layouts/maya.desktop
/usr/share/kmahjongg/layouts/maya.layout
/usr/share/kmahjongg/layouts/maze.desktop
/usr/share/kmahjongg/layouts/maze.layout
/usr/share/kmahjongg/layouts/mesh.desktop
/usr/share/kmahjongg/layouts/mesh.layout
/usr/share/kmahjongg/layouts/moth.desktop
/usr/share/kmahjongg/layouts/moth.layout
/usr/share/kmahjongg/layouts/order.desktop
/usr/share/kmahjongg/layouts/order.layout
/usr/share/kmahjongg/layouts/pattern.desktop
/usr/share/kmahjongg/layouts/pattern.layout
/usr/share/kmahjongg/layouts/penta.desktop
/usr/share/kmahjongg/layouts/penta.layout
/usr/share/kmahjongg/layouts/pillars.desktop
/usr/share/kmahjongg/layouts/pillars.layout
/usr/share/kmahjongg/layouts/pirates.desktop
/usr/share/kmahjongg/layouts/pirates.layout
/usr/share/kmahjongg/layouts/pyramid.desktop
/usr/share/kmahjongg/layouts/pyramid.layout
/usr/share/kmahjongg/layouts/rocket.desktop
/usr/share/kmahjongg/layouts/rocket.layout
/usr/share/kmahjongg/layouts/shield.desktop
/usr/share/kmahjongg/layouts/shield.layout
/usr/share/kmahjongg/layouts/spider.desktop
/usr/share/kmahjongg/layouts/spider.layout
/usr/share/kmahjongg/layouts/squares.desktop
/usr/share/kmahjongg/layouts/squares.layout
/usr/share/kmahjongg/layouts/squaring.desktop
/usr/share/kmahjongg/layouts/squaring.layout
/usr/share/kmahjongg/layouts/stadion.desktop
/usr/share/kmahjongg/layouts/stadion.layout
/usr/share/kmahjongg/layouts/stairs.desktop
/usr/share/kmahjongg/layouts/stairs.layout
/usr/share/kmahjongg/layouts/star.desktop
/usr/share/kmahjongg/layouts/star.layout
/usr/share/kmahjongg/layouts/star_ship.desktop
/usr/share/kmahjongg/layouts/star_ship.layout
/usr/share/kmahjongg/layouts/stax.desktop
/usr/share/kmahjongg/layouts/stax.layout
/usr/share/kmahjongg/layouts/swirl.desktop
/usr/share/kmahjongg/layouts/swirl.layout
/usr/share/kmahjongg/layouts/temple.desktop
/usr/share/kmahjongg/layouts/temple.layout
/usr/share/kmahjongg/layouts/the_door.desktop
/usr/share/kmahjongg/layouts/the_door.layout
/usr/share/kmahjongg/layouts/theatre.desktop
/usr/share/kmahjongg/layouts/theatre.layout
/usr/share/kmahjongg/layouts/time_tunnel.desktop
/usr/share/kmahjongg/layouts/time_tunnel.layout
/usr/share/kmahjongg/layouts/tomb.desktop
/usr/share/kmahjongg/layouts/tomb.layout
/usr/share/kmahjongg/layouts/totem.desktop
/usr/share/kmahjongg/layouts/totem.layout
/usr/share/kmahjongg/layouts/tower.desktop
/usr/share/kmahjongg/layouts/tower.layout
/usr/share/kmahjongg/layouts/triangle.desktop
/usr/share/kmahjongg/layouts/triangle.layout
/usr/share/kmahjongg/layouts/up&down.desktop
/usr/share/kmahjongg/layouts/up&down.layout
/usr/share/kmahjongg/layouts/well.desktop
/usr/share/kmahjongg/layouts/well.layout
/usr/share/metainfo/org.kde.kmahjongg.appdata.xml
/usr/share/qlogging-categories6/kmahjongg.categories
/usr/share/qlogging-categories6/kmahjongg.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmahjongg/config.png
/usr/share/doc/HTML/ca/kmahjongg/config_background.png
/usr/share/doc/HTML/ca/kmahjongg/config_layout.png
/usr/share/doc/HTML/ca/kmahjongg/config_tiles.png
/usr/share/doc/HTML/ca/kmahjongg/gamescreen.png
/usr/share/doc/HTML/ca/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/ca/kmahjongg/index.docbook
/usr/share/doc/HTML/ca/kmahjongg/numbered.png
/usr/share/doc/HTML/cs/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/cs/kmahjongg/index.docbook
/usr/share/doc/HTML/de/kmahjongg/config.png
/usr/share/doc/HTML/de/kmahjongg/config_background.png
/usr/share/doc/HTML/de/kmahjongg/config_layout.png
/usr/share/doc/HTML/de/kmahjongg/config_tiles.png
/usr/share/doc/HTML/de/kmahjongg/gamescreen.png
/usr/share/doc/HTML/de/kmahjongg/highscore.png
/usr/share/doc/HTML/de/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/de/kmahjongg/index.docbook
/usr/share/doc/HTML/de/kmahjongg/numbered.png
/usr/share/doc/HTML/de/kmahjongg/shortcuts.png
/usr/share/doc/HTML/en/kmahjongg/boardeditor.png
/usr/share/doc/HTML/en/kmahjongg/config.png
/usr/share/doc/HTML/en/kmahjongg/config_background.png
/usr/share/doc/HTML/en/kmahjongg/config_layout.png
/usr/share/doc/HTML/en/kmahjongg/config_tiles.png
/usr/share/doc/HTML/en/kmahjongg/gamescreen.png
/usr/share/doc/HTML/en/kmahjongg/highscore.png
/usr/share/doc/HTML/en/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/en/kmahjongg/index.docbook
/usr/share/doc/HTML/en/kmahjongg/numbered.png
/usr/share/doc/HTML/es/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/es/kmahjongg/index.docbook
/usr/share/doc/HTML/et/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/et/kmahjongg/index.docbook
/usr/share/doc/HTML/fr/kmahjongg/config.png
/usr/share/doc/HTML/fr/kmahjongg/config_background.png
/usr/share/doc/HTML/fr/kmahjongg/config_layout.png
/usr/share/doc/HTML/fr/kmahjongg/config_tiles.png
/usr/share/doc/HTML/fr/kmahjongg/gamescreen.png
/usr/share/doc/HTML/fr/kmahjongg/highscore.png
/usr/share/doc/HTML/fr/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/fr/kmahjongg/index.docbook
/usr/share/doc/HTML/fr/kmahjongg/numbered.png
/usr/share/doc/HTML/fr/kmahjongg/shortcuts.png
/usr/share/doc/HTML/it/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/it/kmahjongg/index.docbook
/usr/share/doc/HTML/lt/kmahjongg/config.png
/usr/share/doc/HTML/lt/kmahjongg/config_background.png
/usr/share/doc/HTML/lt/kmahjongg/config_layout.png
/usr/share/doc/HTML/lt/kmahjongg/config_tiles.png
/usr/share/doc/HTML/lt/kmahjongg/gamescreen.png
/usr/share/doc/HTML/lt/kmahjongg/highscore.png
/usr/share/doc/HTML/lt/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/lt/kmahjongg/index.docbook
/usr/share/doc/HTML/lt/kmahjongg/numbered.png
/usr/share/doc/HTML/lt/kmahjongg/shortcuts.png
/usr/share/doc/HTML/nl/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/nl/kmahjongg/index.docbook
/usr/share/doc/HTML/pl/kmahjongg/config.png
/usr/share/doc/HTML/pl/kmahjongg/config_background.png
/usr/share/doc/HTML/pl/kmahjongg/config_layout.png
/usr/share/doc/HTML/pl/kmahjongg/config_tiles.png
/usr/share/doc/HTML/pl/kmahjongg/gamescreen.png
/usr/share/doc/HTML/pl/kmahjongg/highscore.png
/usr/share/doc/HTML/pl/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/pl/kmahjongg/index.docbook
/usr/share/doc/HTML/pl/kmahjongg/numbered.png
/usr/share/doc/HTML/pl/kmahjongg/shortcuts.png
/usr/share/doc/HTML/pt/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/pt/kmahjongg/index.docbook
/usr/share/doc/HTML/pt_BR/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmahjongg/index.docbook
/usr/share/doc/HTML/ru/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/ru/kmahjongg/index.docbook
/usr/share/doc/HTML/sl/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/sl/kmahjongg/index.docbook
/usr/share/doc/HTML/sv/kmahjongg/boardeditor.png
/usr/share/doc/HTML/sv/kmahjongg/config.png
/usr/share/doc/HTML/sv/kmahjongg/gamescreen.png
/usr/share/doc/HTML/sv/kmahjongg/highscore.png
/usr/share/doc/HTML/sv/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/sv/kmahjongg/index.docbook
/usr/share/doc/HTML/sv/kmahjongg/numbered.png
/usr/share/doc/HTML/sv/kmahjongg/shortcuts.png
/usr/share/doc/HTML/sv/kmahjongg/showremoved.png
/usr/share/doc/HTML/uk/kmahjongg/boardeditor.png
/usr/share/doc/HTML/uk/kmahjongg/config.png
/usr/share/doc/HTML/uk/kmahjongg/config_background.png
/usr/share/doc/HTML/uk/kmahjongg/config_layout.png
/usr/share/doc/HTML/uk/kmahjongg/config_tiles.png
/usr/share/doc/HTML/uk/kmahjongg/gamescreen.png
/usr/share/doc/HTML/uk/kmahjongg/highscore.png
/usr/share/doc/HTML/uk/kmahjongg/index.cache.bz2
/usr/share/doc/HTML/uk/kmahjongg/index.docbook
/usr/share/doc/HTML/uk/kmahjongg/numbered.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmahjongg/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kmahjongg/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kmahjongg/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmahjongg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kmahjongg.lang
%defattr(-,root,root,-)


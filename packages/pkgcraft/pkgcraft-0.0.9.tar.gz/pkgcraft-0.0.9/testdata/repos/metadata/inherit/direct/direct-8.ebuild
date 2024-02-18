EAPI=8
inherit a
DESCRIPTION="ebuild with direct eclass inherit"
HOMEPAGE="https://github.com/pkgcraft"
SRC_URI="https://github.com/pkgcraft/pkgcraft-9999.tar.xz"
SLOT=0
LICENSE="l1"

# incrementals
BDEPEND="cat/pkg ebuild/pkg"
DEPEND="cat/pkg ebuild/pkg"
IDEPEND="cat/pkg ebuild/pkg"
PDEPEND="cat/pkg ebuild/pkg"
RDEPEND="cat/pkg ebuild/pkg"

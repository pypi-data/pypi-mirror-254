EAPI=8
DESCRIPTION="ebuild with pkg_pretend failure"
SLOT=0

pkg_pretend() {
	return 1
}

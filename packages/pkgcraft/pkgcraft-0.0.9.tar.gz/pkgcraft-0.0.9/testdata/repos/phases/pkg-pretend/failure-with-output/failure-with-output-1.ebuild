EAPI=8
DESCRIPTION="ebuild with pkg_pretend failure and output"
SLOT=0

pkg_pretend() {
	echo output123
	return 1
}

EAPI=8
DESCRIPTION="ebuild with multi-line LICENSE"
SLOT=0
IUSE="u"
LICENSE="
	l1
	u? (
		l2
	)
"

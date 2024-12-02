pkgname=flatrun-git
pkgver=1.0.0
pkgrel=1
pkgdesc="Runs flatpaks without having to type out their full ids"
arch=(any)
url="https://github.com/nooneisback/FlatpakRunner"
license=('GPL')
depends=('flatpak' 'python')
source=('https://github.com/nooneisback/FlatpakRunner.git')
sha256sums=("SKIP")

package() {
    mkdir -p "${pkgdir}/usr/bin"
    echo "${srcdir}"
    cp "${srcdir}/flatrun.sh" "${pkgdir}/usr/bin/flatrun"
    cp "${srcdir}/flatrun.py" "${pkgdir}/usr/bin/flatrun.py"
    chmod +x "${pkgdir}/usr/bin/flatrun"
    chmod +x "${pkgdir}/usr/bin/flatrun.py"
}

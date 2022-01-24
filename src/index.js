import useHashRouting from './util/router.js'
import NavbarIcons from './components/NavbarIcons.svelte'
import settings from './settings.json'

const navUl = document.querySelector('nav ul')

if(settings.navbarIcons && navUl){
    new NavbarIcons({
        target: navUl
    })
}

if(settings.withHashRouting){
    useHashRouting()
}

if(settings.mainLayout == 'offcanvas-and-article'){
    const header = document.querySelector('header')
    const tocShowButton = document.querySelector('#toc-show')

    const tocShowCallback = (entries) => {
        entries.forEach(entry => {
            if(entry.target !== header) return
            tocShowButton.style.top = entry.isIntersecting ? "var(--header-height)" : "0"
        })
    }

    const tocShowObserver = new IntersectionObserver(tocShowCallback, {threshold: .25});


    tocShowObserver.observe(header)
}

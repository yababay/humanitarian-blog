import useHashRouting from './util/router.js'
import NavbarIcons from './components/NavbarIcons.svelte'
import AsideLinks  from './components/AsideLinks.svelte'
import settings from './settings.json'

const navUl = document.querySelector('nav ul')

if(settings.navbarIcons && navUl){
    new NavbarIcons({
        target: navUl
    })
}

const asideUls = document.querySelectorAll('aside ul')

new AsideLinks({
    target: asideUls[0],
    props: {year: '2022'}
})

new AsideLinks({
    target: asideUls[1],
    props: {year: '2021'}
})

if(settings.withHashRouting){
    useHashRouting()
}

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

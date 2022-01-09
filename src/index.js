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

const asideUl = document.querySelector('aside ul')

new AsideLinks({
    target: asideUl
})

if(settings.withHashRouting){
    useHashRouting()
}


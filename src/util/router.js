import StaticPage  from '../pages/StaticPage.svelte'
import BackendPage from '../pages/BackendPage.svelte'

const home = 'welcome'
const articleElement = document.querySelector('article')

let lastURL = document.URL;

window.addEventListener("hashchange", function(event){
    Object.defineProperty(event, "oldURL", {enumerable:true,configurable:true,value:lastURL})
    Object.defineProperty(event, "newURL", {enumerable:true,configurable:true,value:document.URL})
    lastURL = document.URL;
    switchHash()
});

function switchHash(){
    const url = document.URL
    if(!url.includes('#')) return
    let link = /.*#([a-zA-Z0-9\-\/\._\:]+)$/.exec(url)
    if(!(link && link[1])) link = home
    else {
        link = link[1] 	
        if(link == '/') link = home
    }
    articleElement.innerHTML = ''
    const Fn = /^\/api($|\/.*)/.test(link) ? BackendPage : StaticPage
    new Fn({
        target: articleElement, 
        props: {link}
    })
}

export default switchHash


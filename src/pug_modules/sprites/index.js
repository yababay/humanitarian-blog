#!/usr/bin/env node

const fs = require('fs')
const prefix = "../../../node_modules/bootstrap-icons/icons/"

console.log('<svg style="display: none">')

//for(const fn of process.argv){
for(const fn of ['github', 'telegram', 'medium', 'person-plus', 'blockquote-left']){
    const path = `${prefix}/${fn}.svg`
    if(!fs.existsSync(path)) continue
    let svg = fs.readFileSync(path).toString()
    svg = svg.replace(/<svg[^>]+>/, `<symbol id="${fn}" viewBox="0 0 16 16" fill="currentColor">`)
    svg = svg.replace('</svg>', '</symbol>')
    console.log(svg)
}

console.log('</svg>')

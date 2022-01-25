<script>
    import Showdown from 'showdown'

    const converter = new Showdown.Converter()
    const tocClose = document.querySelector('#toc-offcanvas .btn-close')

    export let link
    export let prefix = 'content'

    let isEditMode = false
    let editor

    const isLocal = document.URL.includes('localhost')

    async function getMarkup() {
        const res = await fetch(`${prefix}/${link}${link.endsWith(".md") ? "" : ".md"}`)
        if(res.status != 200) throw "Не удалось загрузить запрашиваемый ресурс."
        const txt = await res.text()
        closeOffcanvas()
        return converter.makeHtml(txt)
    }

    function closeOffcanvas(){
        if(tocClose) tocClose.click()
        return ''
    }

    async function toggleEditing(){
        isEditMode = !isEditMode
        if(isEditMode){
            const res = await fetch(`${prefix}/${link}${link.endsWith(".md") ? "" : ".md"}`)
            if(res.status != 200) return
            editor.value = await res.text()
        }
        else {
            const res = await fetch(`/api/save/${link}`, {method: 'post', headers: {"Content-Type": "text/plain"}, body: editor.value.trim()})
            if(res.status != 200) return alert('Не удалось сохранить файл.')
        }
    }

</script>

<section class="container">
    {#if isLocal}
        <p class="text-end button-holder">
        <button class="btn btn-primary" on:click={async e => await toggleEditing()}>{isEditMode ? "Сохранить" : "Редактировать"}</button>
        </p>
    {/if}
    {#if !isEditMode}
        {#await getMarkup() then markup}
            <div class="comfortable-reading mt-3">
                {@html markup}
            </div>
        {:catch error}
            <div class="alert alert-danger text-center mt-3" role="alert">
                {error + closeOffcanvas()}
            </div>
        {/await}
    {:else}
        <textarea class="form-control editor" bind:this={editor}/>
    {/if}
</section>    

<style>
    .comfortable-reading {
        max-width: 80ch;
    }
    .button-holder {
        margin: 2rem 0 2rem 0;
    }
    .editor {
        height: 640px;
        width: 100%;
    }
</style>

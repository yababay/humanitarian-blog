<script>
    let form

    function send(e){
        e.preventDefault()
        const title = form.title.value
        const date = form.date.value
        const url = new URL(document.URL) //new URL("/api/initialize") // + new URLSearchParams({title, date}))
        url.hash = ''
        url.pathname = "/api/initialize"    
        url.searchParams.set('title', title)    
        url.searchParams.set('date', date)    
            fetch(url).then(res => res.text()).then(txt => alert(txt) || form.reset())
    }

</script>

<form action="/api/initialize" bind:this={form} on:submit={send}>
    <fieldset class="fieldset">
        <legend>Создать новый текст</legend>
        <p>
            <input name="title"  class="form-control" placeholder="Заголовок">
        </p>
        <p>
            <input name="date" class="form-control" placeholder="Дата публикации">
        </p>
        <p class="text-end">
            <input type="submit" class="btn btn-primary mb-3" value="Выгрузить">
        </p>
    <fieldset>
</form> 

<style>
    .fieldset {
        max-width: 50rem;
        margin: 3rem auto;
    }
</style>

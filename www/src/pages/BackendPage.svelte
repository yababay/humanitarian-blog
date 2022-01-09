<script>
    import Initializer from '../components/Initializer.svelte'

    export let link
</script>    

{#if link == '/api/initialize'}
    <Initializer />
{/if}


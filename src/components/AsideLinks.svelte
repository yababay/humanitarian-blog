<script>
    import Icon from '@yababay67/svelte-meets-bootstrap-icons/blockquote-left.svelte'
    import { onMount } from 'svelte'
    export let year

    async function getTocByYear(){
        const res = await fetch('toc.json')
        let posts = await res.json()
        posts = posts.filter(el => el[0].includes('#' + year))
        return posts
    }

</script>

{#await getTocByYear() then posts}
    {#each posts as post}
        <li>
            <a href={post[0]} class="nav-link link-secondary">
                <Icon size="24" />
                {`${post[1]} (${post[2]})`}
            </a>
        </li>
    {/each}
{/await}


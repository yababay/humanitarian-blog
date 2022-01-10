<script>
    import Icon from '@yababay67/svelte-meets-bootstrap-icons/blockquote-left.svelte'
    import { onMount } from 'svelte'
    let isLocalhost = new URL(document.URL).host.includes('localhost')
</script>

{#await fetch(isLocalhost ? '/api/toc' : 'toc.json').then(res => res.json()) then posts}
    {#each posts as post}
        <li>
            <a href={post[0]} class="nav-link link-secondary">
                <Icon size="24" />
                {`${post[1]} (${post[2]})`}
            </a>
        </li>
    {/each}
{/await}


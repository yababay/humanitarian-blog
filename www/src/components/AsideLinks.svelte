<script>
    import BookIcon from '@yababay67/svelte-meets-bootstrap-icons/book.svelte'
    import SignpostIcon from '@yababay67/svelte-meets-bootstrap-icons/signpost.svelte'
</script>

{#await fetch('toc.json').then(res => res.json()) then posts}
    {#each posts as post}
        <li>
            <a href={post[0]} class="nav-link link-secondary">
                <SignpostIcon size="24" />
                {`${post[1]} (${post[2]})`}
            </a>
        </li>
    {/each}
{/await}


<script>
    import settings from '../settings.json'
    import Github from './iconified-links/Github.svelte'
    import Initialize from './iconified-links/Initialize.svelte'
    import Community from './iconified-links/Community.svelte'
</script>

{#each settings.navbarIcons as link}
    {#if link.icon == 'initialize'}
        <Initialize />
    {/if}
    {#if link.icon == 'github'}
        <Github />
    {/if}
    {#if link.icon == 'community'}
        <Community />
    {/if}
{/each}

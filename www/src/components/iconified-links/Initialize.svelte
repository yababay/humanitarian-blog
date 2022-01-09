<script>
    import Icon from '@yababay67/svelte-meets-bootstrap-icons/pencil.svelte'
    import settings from '../../settings.json'

    export let link = '#/api/initialize'
    export let title = 'Редактировать'
    export let size = 32
    const props = {title, size}
</script>

<li class="navbar-item icon-holder ms-3">
    <a class="navbar-link link-secondary" href={link}>
        <Icon {...props}/>
    </a>
</li>


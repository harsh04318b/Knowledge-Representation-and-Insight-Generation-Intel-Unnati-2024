<script>
    import { onMount } from "svelte";

    let htmlcontent = ""
    onMount(async()=>{
        const response =  await fetch('/Knowledge_Representation.html')
        htmlcontent = await response.text()
    })
</script>
<main>
    <div class="m-4 mr-48 ml-48 h-96 overflow-auto p-4">
        {@html htmlcontent}
    </div>
</main>
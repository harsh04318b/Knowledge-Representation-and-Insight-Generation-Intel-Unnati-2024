<script>
  import { goto } from "$app/navigation";

  function navigate() {
    goto("/custom");
  }
</script>

<header class="bg-[#F5F5DC] py-4">
  <div class="flex items-center justify-between">
    <h1 class="text-[#2E4053] text-3xl font-bold ml-8">
      Knowledge Representation and Data Analysis
    </h1>
    <button on:click={navigate} class="mr-8 p-4 pt-2 pb-2 bg-cyan-500 rounded-3xl">custom inputs Page</button>
  </div>
</header>

<script>
  import Hero from "../Components/Hero.svelte";
  import Description from "../Components/Description.svelte";
  import Insights from "../Components/Insights.svelte";
  import Model from "../Components/Model.svelte";

  function download() {
    const url = "/Knowledge_Representation.ipynb";
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.setAttribute("download", "Knowledge_Representation.ipynb");
    anchor.click();
  }

  function download_model() {
    const url = "/Models.ipynb";
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.setAttribute("download", "Models.ipynb");
    anchor.click();
  }
</script>

<main>
  <section>
    <div class="data-table card">
      <p class="flex text-3xl items-center justify-center">Heart Disease</p>
      <Hero />
    </div>
  </section>

  <section>
    <div class="section-header">
      <h2>Ed Analysis and Insight Generation</h2>
      <button on:click={download}>Download the Colab File</button>
    </div>
    <div class="cards-container">
      <Description />
      <Insights />
    </div>
  </section>

  <section>
    <div class="section-header">
      <h2>ML Models</h2>
      <button on:click={download_model}>Download Colab File</button>
    </div>
    <div class="card">
      <Model />
    </div>
  </section>
</main>

<style>
  main {
    padding: 20px;
    font-family: Arial, sans-serif;
  }

  section {
    margin-bottom: 40px;
  }

  .section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .section-header h2 {
    margin: 0;
    font-size: 1.75rem;
  }

  button {
    background-color: #00bcd4;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #00acc1;
  }

  .card {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .cards-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }

  .card p {
    margin: 0 0 10px;
  }

  .data-table {
    width: 100%;
    overflow-x: auto;
    margin-bottom: 20px;
  }
</style>

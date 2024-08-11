<script>
  import Papa from "papaparse";
  import { onMount } from "svelte";

  let csvData = [];

  onMount(async () => {
    const response = await fetch("/data.csv");
    const csvText = await response.text();
    Papa.parse(csvText, {
      header: true,
      complete: function (results) {
        csvData = results.data;
      },
    });
  });
  function download() {
    const url = '/data.csv';
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.setAttribute('download', 'data.csv');
    anchor.click();
  }
</script>

<main class="flex">
  <div class="bg-white border border-red-500 size-3/4 h-96 m-4">
    <div class="table-container">
      <table>
        <thead>
          <tr>
            {#if csvData.length > 0}
              {#each Object.keys(csvData[0]) as key}
                <th>{key}</th>
              {/each}
            {/if}
          </tr>
        </thead>
        <tbody>
          {#each csvData as row}
            <tr>
              {#each Object.values(row) as value}
                <td>{value}</td>
              {/each}
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
    <button class="p-4 pt-2 pb-2 bg-cyan-700 text-slate-100 rounded-3xl" on:click={download}>
        Download CSV
      </button>
  </div>
  <div class="flex flex-col border border-red-500 w-1/4 h-96 m-4 p-4">
    <p class="text-center font-bold text-lg mb-2">About the Dataset</p>
    <p class="text-justify">
        The World Health Organization reports 12 million annual deaths from heart diseases globally, with half in developed countries. Early prognosis can guide lifestyle changes in high-risk patients to reduce complications. This study uses logistic regression to identify key risk factors and predict heart disease risk. The dataset, sourced from Kaggle, stems from a cardiovascular study in Framingham, Massachusetts, comprising over 4,000 records and 15 attributes.
    </p>
</div>

</main>

<style>
  .table-container {
    max-height: 400px; 
    overflow-y: auto;
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
  }

  th,
  td {
    border: 1px solid #ddd;
    padding: 8px;
  }

  th {
    background-color: #f2f2f2;
    position: sticky;
    top: 0;
    z-index: 1;
  }
</style>

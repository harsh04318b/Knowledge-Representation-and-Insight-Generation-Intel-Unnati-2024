<!-- src/Components/Predict.svelte -->
<script>
  import Graphs from "../../Components/Graphs.svelte";
  import { onMount } from "svelte";
  import axios from "axios";
  let male,
    age,
    currentSmoker,
    cigsPerDay,
    BPMeds,
    prevalentStroke,
    prevalentHyp,
    diabetes,
    totChol,
    sysBP,
    diaBP,
    BMI,
    heartRate,
    glucose;
  let prediction = "";
  let error = "";

  const predict = async () => {
    try {
      error = "";
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        male: +male,
        age: +age,
        currentSmoker: +currentSmoker,
        cigsPerDay: +cigsPerDay,
        BPMeds: +BPMeds,
        prevalentStroke: +prevalentStroke,
        prevalentHyp: +prevalentHyp,
        diabetes: +diabetes,
        totChol: +totChol,
        sysBP: +sysBP,
        diaBP: +diaBP,
        BMI: +BMI,
        heartRate: +heartRate,
        glucose: +glucose,
      });
      prediction = response.data.result;
      console.log("Prediction:", prediction);
    } catch (err) {
      console.error("Error:", err);
      error = "An error occurred while making the prediction.";
      prediction = "";
    }
  };
</script>

<div class="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-md">
  <Graphs />
  <div>
    <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">
      Heart Disease Prediction
    </h2>
    <form on:submit|preventDefault={predict} class="space-y-4">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <input
          type="number"
          bind:value={male}
          placeholder="Male (1 or 0)"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={age}
          placeholder="Age"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={currentSmoker}
          placeholder="Current Smoker (1 or 0)"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={cigsPerDay}
          placeholder="Cigs Per Day"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={BPMeds}
          placeholder="BP Meds (1 or 0)"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={prevalentStroke}
          placeholder="Prevalent Stroke (1 or 0)"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={prevalentHyp}
          placeholder="Prevalent Hyp (1 or 0)"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={diabetes}
          placeholder="Diabetes (1 or 0)"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={totChol}
          placeholder="Total Cholesterol"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={sysBP}
          placeholder="Systolic BP"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={diaBP}
          placeholder="Diastolic BP"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={BMI}
          placeholder="BMI"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={heartRate}
          placeholder="Heart Rate"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          bind:value={glucose}
          placeholder="Glucose"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <button
        type="submit"
        class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition duration-300"
        >Predict</button
      >
    </form>

    {#if error}
      <p class="mt-4 text-red-600">{error}</p>
    {:else if prediction}
      <p class="mt-4 text-lg font-semibold text-green-600">
        Prediction: <span class="  text-purple-400 font-bold text-lg">{prediction}</span> in the next 10 years
      </p>
    {/if}
  </div>
</div>

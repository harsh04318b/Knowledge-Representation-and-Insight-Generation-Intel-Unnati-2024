<script>
  const descriptions = [
    { name: "male", desc: "Gender (1 = Male, 0 = Female). Indicates the gender of the individual." },
    { name: "age", desc: "Age in years. Represents the age of the individual." },
    { name: "currentSmoker", desc: "Currently smoking (1 = Yes, 0 = No). Indicates if the individual is a current smoker." },
    { name: "cigsPerDay", desc: "Cigarettes per day. Number of cigarettes the individual smokes per day." },
    { name: "BPMeds", desc: "Blood pressure medication (1 = Yes, 0 = No). Indicates if the individual is on blood pressure medication." },
    { name: "prevalentStroke", desc: "History of stroke (1 = Yes, 0 = No). Indicates if the individual has a history of stroke." },
    { name: "prevalentHyp", desc: "Prevalent hypertension (1 = Yes, 0 = No). Indicates if the individual has prevalent hypertension." },
    { name: "diabetes", desc: "Diabetes (1 = Yes, 0 = No). Indicates if the individual has diabetes." },
    { name: "totChol", desc: "Total cholesterol. Measures the total cholesterol level in the blood." },
    { name: "sysBP", desc: "Systolic blood pressure. Measures the systolic blood pressure." },
    { name: "diaBP", desc: "Diastolic blood pressure. Measures the diastolic blood pressure." },
    { name: "BMI", desc: "Body mass index. A measure of body fat based on height and weight." },
    { name: "heartRate", desc: "Heart rate. Measures the heart rate in beats per minute." },
    { name: "glucose", desc: "Glucose level. Measures the glucose level in the blood." },
    { name: "TenYearCHD", desc: "Ten-year risk of coronary heart disease (1 = Yes, 0 = No). Indicates the ten-year risk of developing coronary heart disease." }
  ];
</script>

<style>
  .scroll-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 10px;
    overflow-x: auto;
    white-space: nowrap;
    padding: 10px;
    border: 1px solid #ccc;
  }
  .item {
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .item strong {
    display: block;
    margin-bottom: 5px;
    text-transform: capitalize;
    color: #543310;
  }
</style>

<div class="scroll-container">
  {#each descriptions as { name, desc }}
    <div class="item">
      <strong>{name}:</strong> {desc}
    </div>
  {/each}
</div>
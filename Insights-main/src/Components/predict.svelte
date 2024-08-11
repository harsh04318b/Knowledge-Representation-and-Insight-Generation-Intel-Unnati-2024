<script>
    import axios from 'axios';
    let xInput = '';
    let prediction = '';

    const getPrediction = async () => {
        try {
            const response = await axios.post('http://localhost:5000/predict', { x: [parseFloat(xInput)] });
            prediction = response.data[0];
        } catch (error) {
            console.error(error);
        }
    }
</script>

<main>
    <h1>Linear Regression Predictor</h1>
    <input type="number" bind:value={xInput} placeholder="Enter a number" />
    <button on:click={getPrediction}>Predict</button>
    {#if prediction !== ''}
        <p>Prediction: {prediction}</p>
    {/if}
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    input, button {
        margin: 10px;
    }
</style>

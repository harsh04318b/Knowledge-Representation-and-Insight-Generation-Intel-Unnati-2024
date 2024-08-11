<script>
    import axios from 'axios';
    
    let file;
    let graphs = [];
    let error = '';
    let loading = false;

    async function handleSubmit() {
        const formData = new FormData();
        formData.append('file', file);

        loading = true;
        try {
            const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                },
                responseType: 'json'
            });
            graphs = response.data.graphs;
            error = '';
        } catch (err) {
            console.error('Error:', err);
            error = err.response?.data?.error || 'An error occurred while processing the file.';
            graphs = [];
        } finally {
            loading = false;
        }
    }
</script>

<div class="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-md">
    <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Dataset Analysis & Insight Generation</h2>
    
    <form on:submit|preventDefault={handleSubmit} class="mb-6">
        <div class="mb-4">
            <label for="fileUpload" class="block text-sm font-medium text-gray-700 mb-2">
                Upload Dataset (CSV)  *please upload the appropriate type
            </label>
            <input 
                id="fileUpload"
                type="file" 
                accept=".csv"
                on:change={e => file = e.target.files[0]}
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
        </div>
        <button 
            type="submit" 
            class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition duration-300"
            disabled={loading}
        >
            {loading ? 'Analyzing...' : 'Analyze Dataset'}
        </button>
    </form>

    {#if error}
        <p class="text-red-600 mb-4">{error}</p>
    {/if}

    {#if graphs.length > 0}
        <div class="space-y-6">
            {#each graphs as graph}
                <div class="border rounded-lg p-4">
                    <h3 class="text-lg font-semibold mb-2">{graph.title}</h3>
                    <img src={`data:image/png;base64,${graph.image}`} alt={graph.title} class="w-full" />
                </div>
            {/each}
        </div>
    {/if}
</div>

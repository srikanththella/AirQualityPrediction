document.getElementById("inputForm").addEventListener("submit",async function(event) {
    event.preventDefault();

    const temp = document.getElementById("temp").value;
    const no2 = document.getElementById("no2").value;
    const so2 = document.getElementById("so2").value;
    const co = document.getElementById("co").value;
    const industrial = document.getElementById("industrial").value;

    const data = {
        temperature : temp,
        no2: no2,
        so2: so2,
        co: co,
        proximity_to_industrial_areas: industrial
    };

    try{
        const response = await fetch('/predict',{method:'POST',headers:{'Content-Type': 'application/json'},
        body: JSON.stringify(data)});

        const result = await response.json();
        const prediction = result.prediction === 1?"Good Air":"Poor Air";
        document.getElementById("predictionResult").innerHTML = 'Prediction: ${prediction}';
    } catch(error){
        console.error("Error:",error);
    }
});
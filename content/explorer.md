---
title: "Data Explorer"
url: /explorer
---

Explore, search and add datasets.


#### IndicNLP: Current Status

Status of datasets across languages:

<div id="status">
</div>


#### Search Datasets

<link rel="stylesheet" href="https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css">
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
<script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>

<script>

    let dataURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQGyB-QInM69IoR2nP6pJ_Uc0tA0fRxb1NvDe1F1GvBd7UT9lYW06-DuTjaKTYzmuHbAEPaQR5nhhCb/pub?gid=0&single=true&output=csv";
    let encodedURL = encodeURIComponent(dataURL)
    let proxyURL = `https://api.allorigins.win/raw?url=${encodedURL}`;
    console.log(proxyURL);

    result = Papa.parse(proxyURL, {
        download: true,
        dynamicTyping: true,
        complete: function(results) {
            let data = process_data(results.data);
            let table = [];
            for (const prop in data.datasets) {
                for (const lang in data.datasets[prop]) {
                    for (const name of data.datasets[prop][lang]) {
                        table.push([name, prop, lang]);
                    }
                }
            }
            $('#example').DataTable( {
                data: table,
                columns: [
                    { title: "Dataset Name" },
                    { title: "Dataset Type" },
                    { title: "Language" },
                ]
            });
            for (const type in data.datasets) {
                $("#status").append(`<span class="badge badge-info">${type}</span> ${Object.keys(data.datasets[type]).join(" ")}<br>`);
            }
        }
    });

    function process_data(data) {
        window.data = data;
        let languages = data[0].slice(2, 14);
        languages = languages.map(l => l.trim());

        let dataset_types = data.slice(2).map(row => row[0]);

        let datasets = {};
        for (let i = 2; i < data.length; i++) {
            let row = data[i];
            let type = row[0];
            if (!(type in datasets)) {
                datasets[type] = {};
            }
            for (let j = 2; j < languages.length; j++) {
                let lang = languages[j-1]
                if (row[j] !== null) {
                    datasets[type][lang] = row[j].split("\n");
                }
            }
        }
        return {
            languages: languages,
            dataset_types: dataset_types,
            datasets: datasets
        };
    }

</script>

<table id="example">
</table>


#### Add a Dataset

<div style="width: 50%; max-width: 300px;">
Dataset type: <input class="form-control" type="text"/>
Link: <input class="form-control" type="text">
</div>

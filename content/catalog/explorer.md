---
title: "Data Explorer"
url: /explorer
weight: 0
---

Explore, search and add datasets.


### IndicNLP: The Current State


<table id="example2" class="ui table table-bordered dt-responsive no-wrap compact unstackable">
</table>

### Search Datasets


<link rel="stylesheet" href="https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css">
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
<script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
<style>
    table.dataTable.no-footer {
        border-bottom: 0 !important;
    }

    tfoot {
        display: table-row-group;
    }
    input[type="text"] {
     width: 100%; 
     box-sizing: border-box;
     -webkit-box-sizing:border-box;
     -moz-box-sizing: border-box;
    }


</style>

<script>

    let dataURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQGyB-QInM69IoR2nP6pJ_Uc0tA0fRxb1NvDe1F1GvBd7UT9lYW06-DuTjaKTYzmuHbAEPaQR5nhhCb/pub?gid=0&single=true&output=csv";
    let encodedURL = encodeURIComponent(dataURL)
    let proxyURL = `https://api.allorigins.win/raw?url=${encodedURL}`;

    result = Papa.parse(proxyURL, {
        download: true,
        dynamicTyping: true,
        complete: function(results) {
            let data = process_data(results.data);
            let dataset_names = {};
            for (const type in data.datasets) {
                for (const lang in data.datasets[type]) {
                    for (const name of data.datasets[type][lang]) {
                        if (!(name in dataset_names)) {
                            dataset_names[name] = {};
                        }
                        if (!(type in dataset_names[name])) {
                            dataset_names[name][type] = []
                        }
                        dataset_names[name][type].push(lang);
                    }
                }
            }
            let table = [];
            for (const name in dataset_names) {
                for (const type in dataset_names[name]) {
                    table.push([name, type, dataset_names[name][type].sort().join(", "), `<div id="${name}"></div>`]);
                }
            }
            $('#example').DataTable( {
                data: table,
                columns: [
                    { title: "Dataset Name" },
                    { title: "Dataset Type" },
                    { title: "Language" },
                    { title: "Link"}
                ],
                pageLength: 10,
                "lengthChange": false,
                "ordering": false,
                // dom: 'lrtp',
                initComplete: function () {
                    /*
                    $("#example").append(
                        $('<tfoot/>').append( $("#example thead tr").clone() )
                    );
                    $('tfoot').each(function () {
                        $(this).insertAfter($(this).siblings('thead'));
                    });
                    $('#example tfoot th').each( function () {
                        var title = $(this).text();
                        $(this).html( '<div class="ui input"><input type="text" placeholder="Search '+title+'" /></div>' );
                    });

                    // Apply the search
                    window.dt = this;
                    this.api().columns().every( function () {
                        var that = this;
                        $('input', this.footer()).on('keyup change clear', function () {
                            if ( that.search() !== this.value ) {
                                that.search( this.value ).draw();
                            }
                        });
                    });
                    
                    */
                }
            });
            let table2 = [];
            for (const type in data.datasets) {
                let row = [type];
                for (let lang of data.languages) {
                    if (lang in data.datasets[type]) {
                        row.push(`<i class="green icon check"></span>`);
                    } else {
                        row.push(`<i class="red close icon"></i>`);
                    }
                }
                table2.push(row);
                // table2.push([type, Object.keys(data.datasets[type]).join(", ")]);
            }
            let columns =  [{ title: "Dataset Type" }];
            for (let lang of data.languages) {
                columns.push({title: lang});
            }
            $('#example2').DataTable( {
                data: table2,
                columns: columns,
                "lengthChange": false,
                "ordering": false,
                "info":     false,
                "filter": false,
            });

 
        }
    });

    dataURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQGyB-QInM69IoR2nP6pJ_Uc0tA0fRxb1NvDe1F1GvBd7UT9lYW06-DuTjaKTYzmuHbAEPaQR5nhhCb/pub?gid=1367132144&single=true&output=csv";
    encodedURL = encodeURIComponent(dataURL)
    proxyURL = `https://api.allorigins.win/raw?url=${encodedURL}`;

    result = Papa.parse(proxyURL, {
        download: true,
        dynamicTyping: true,
        complete: function(results) {
            for (let i = 1; i < results.data.length; i++) {
                $("#" + results.data[i][0]).html(`<a href="${results.data[i][1]}">link</a>`);
            }
        }
    });

    function process_data(data) {
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
            for (let j = 2; j < languages.length+2; j++) {
                let lang = languages[j-2]
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

<table id="example" class="ui table table-bordered dt-responsive no-wrap compact">
</table>

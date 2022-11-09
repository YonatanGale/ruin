function generate_report () {
    var parameters = {
        'action': 'search_report',
        'start_date': '2022-11-09',
        'end_date': '2022-11-09'
    };

    $(function (){
        $('#data').DataTable( {
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: parameters,
                dataSrc: ""
            },
            // columns: [
            //     { "data": "id"},
            //     { "data": "name"},
            //     { "data": "id"},
            // ],
            columnDefs: [
                {
                    targets: [-1, -2, -3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Gs'+ parseFloat(data).toFixed(2)
                    }
                },
            ],
            initComplete: function(settings, json) {
            
              }
            });
    });
}

$(function () {
    $('input[name="date_ranger"]').daterangepicker({
        locale : {
            format: 'YYYY-MM-DD'

        }
    });

    generate_report();
});
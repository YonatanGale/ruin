 var tblType;
 var tblfund;

 $(function () {
    tblfund = $('#tblfund').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "amount"},
            {"data": "typeMove"},
            {"data": "PayName"},
            {"data": "payNro"},
            {"data": "payowner"},
            {"data": "date_joined"},
        ],
        columnDefs: [
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return 'Gs.' + parseFloat(data).toFixed(2);
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
        
    tblType= $('#tblType').DataTable({
            responsive: true,
            autoWidth: false,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'TypeList',
                },
                dataSrc: "",
            },
            order: false,
            info: false,
            paging: false,
            searching: false,
            columns: [
                {"data": "name"},
                {"data": "impo"},
            ],
            columnDefs: [
            ],
            initComplete: function (settings, json) {
    
            }
        });
});

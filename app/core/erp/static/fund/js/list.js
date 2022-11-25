 var tblType;
 var tblfund;

 $(function () {
    tblfund = $('#tblfund').DataTable({
        responsive: true,
        autoWidth: false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata',
            },
            dataSrc: "",
        },
        order: false,
        info: false,
        paging: false,
        searching: false,
        columns: [
            {"data": "id"},
            {"data": "amount"},
            {"data": "typeMove"},
            {"data": "methodpay.pay"},
            {"data": "payNro"},
            {"data": "payowner"},
            {"data": "date_joined"},
        ],
        columnDefs: [
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

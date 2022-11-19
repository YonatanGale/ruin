$(function (){
    $('#data').DataTable( {
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action':'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "id"},
            { "data": "first_name"},
            { "data": "last_name"},
            { "data": "ci"},
            { "data": "username"},
            { "data": "date_joined"},
            { "data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/edit/'+row.id+'/" class="btn btn-warning btn-xs"><i class="far fa-edit"></i></a> ';
                    buttons += '<a href="/user/delete/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="far fa-trash-alt"></i></a>';
                    return buttons
                }
            },
        ],
        initComplete: function(settings, json) {
        
          }
        });
});
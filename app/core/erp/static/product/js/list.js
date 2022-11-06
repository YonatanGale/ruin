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
            { "data": "name"},
            { "data": "cate.name"},
            { "data": "price"},
            { "data": "cant"},
            { "data": "cant"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/product/edit/'+row.id+'/" class="btn btn-warning btn-xs"><i class="far fa-edit"></i></a> ';
                    buttons += '<a href="/erp/product/delete/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="far fa-trash-alt"></i></a>';
                    return buttons
                }
            },
        ],
        initComplete: function(settings, json) {
        
          }
        });


});
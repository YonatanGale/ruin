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
            { "data": "full_name"},
            { "data": "ci"},
            { "data": "username"},
            { "data": "date_joined"},
            { "data": "groups"},
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
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                   var html = '';
                   $.each(row.groups, function (key, value) {
                    html+='<span class="badge badge-success">'+value.name+'</span> ';
                   });
                   return html;
                }
            },
        ],
        initComplete: function(settings, json) {
        
          }
        });
});
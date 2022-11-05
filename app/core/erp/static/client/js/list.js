var tblClient;
var modal_title;

function getData(){
    tblClient = $('#data').DataTable( {
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
            { "data": "names"},
            { "data": "surnames"},
            { "data": "ci"},
            { "data": "Birthday"},
            { "data": "addres"},
            { "data": "addres"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs"><i class="far fa-edit"></i></a> ';
                    buttons += '<a href="/erp/client/delete/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="far fa-trash-alt"></i></a>';
                    return buttons
                }
            },
        ],
        initComplete: function(settings, json) {
        
          }
        });
}

$(function () {
    
    modal_title = $('.modal-title');

    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un cliente');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalClient').modal('show');
    });

    $('#data tbody')
    .on('click', 'a[rel="edit"]', function () {
        modal_title.find('span').html('Edición de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblClient.cell($(this).closest('td, li')).index();
        var data = tblClient.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="names"]').val(data.names);
        $('input[name="surnames"]').val(data.surnames);
        $('input[name="ci"]').val(data.ci);
        $('input[name="Birthday"]').val(data.Birthday);
        $('input[name="addres"]').val(data.addres);
        $('#myModalClient').modal('show');
    });


    $('#myModalClient').on('shown.bs.modal', function () {
        // $('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = $(this).serializeArray();
        alert_jqueryconfirm(window.location.pathname, parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
        });
    });
});

var tblSupplier;
var modal_title;

function getData(){
    tblSupplier = $('#data').DataTable( {
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
            { "data": "email"},
            { "data": "phone"},
            { "data": "address"},
            { "data": "address"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs"><i class="far fa-edit"></i></a> ';
                    buttons += '<a href="#" rel="delete" class="btn btn-danger btn-xs"><i class="far fa-trash-alt"></i></a>';
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
        $('#myModalSupplier').modal('show');
    });

    $('#data tbody')
    .on('click', 'a[rel="edit"]', function () {
        modal_title.find('span').html('Edición de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblSupplier.cell($(this).closest('td, li')).index();
        var data = tblSupplier.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="names"]').val(data.names);
        $('input[name="surnames"]').val(data.surnames);
        $('input[name="ci"]').val(data.ci);
        $('input[name="email"]').val(data.email);
        $('input[name="phone"]').val(data.phone);
        $('input[name="address"]').val(data.address);
        $('#myModalSupplier').modal('show');
    })
    .on('click', 'a[rel="delete"]', function () {
        var tr = tblSupplier.cell($(this).closest('td, li')).index();
        var data = tblSupplier.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, parameters, function () {
                tblSupplier.ajax.reload();
            });
        });


    $('#myModalSupplier').on('shown.bs.modal', function () {
        // $('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = $(this).serializeArray();
        alert_jqueryconfirm(window.location.pathname, parameters, function () {
            $('#myModalSupplier').modal('hide');
            tblSupplier.ajax.reload();
        });
    });
});

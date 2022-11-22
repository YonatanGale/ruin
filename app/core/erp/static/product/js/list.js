var tblProduct;
var modal_title;

function getData(){
    tblProduct = $('#data').DataTable( {
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
            { "data": "stock"},
            { "data": "stock"},
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
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if(row.stock > 0){
                        return '<span class="badge badge-success">'+data+'</span>'
                    }
                    return '<span class="badge badge-danger">'+data+'</span>'
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return 'Gs' + parseFloat(data).toLocaleString("es-AR");

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


    $('.btnRecycle').on('click', function () {
        $('input[name="action"]').val('recycle');
        modal_title.find('span').html('Retirar un producto');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-recycle');
        $('form')[0].reset();
        $('#myModalRecycle').modal('show');
    });

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un producto');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalProduct').modal('show');
    });

    $('#data tbody')
    .on('click', 'a[rel="edit"]', function () {
        modal_title.find('span').html('Edición de un producto');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblProduct.cell($(this).closest('td, li')).index();
        var data = tblProduct.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="name"]').val(data.name);
        $('input[name="cate.id"]').val(data.cate);
        $('input[name="price"]').val(data.price);
        $('input[name="stock"]').val(data.stock);
        $('#myModalProduct').modal('show');
    })
    .on('click', 'a[rel="delete"]', function () {
        var tr = tblProduct.cell($(this).closest('td, li')).index();
        var data = tblProduct.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, parameters, function () {
                tblProduct.ajax.reload();
            });
        });


    $('#myModalProduct').on('shown.bs.modal', function () {
        // $('form')[0].reset();
    });

    $('#formrproduct').on('submit', function (e) {
        e.preventDefault();
        var parameters = $(this).serializeArray();
        alert_jqueryconfirm(window.location.pathname, parameters, function () {
            $('#myModalProduct').modal('hide');
            tblProduct.ajax.reload();
        });
    });
    $('#formrecycle').on('submit', function (e) {
        e.preventDefault();
        var parameters = $(this).serializeArray();
        alert_jqueryconfirm(window.location.pathname, parameters, function () {
            $('#myModalRecycle').modal('hide');
            tblProduct.ajax.reload();
        });
    });
});

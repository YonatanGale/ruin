var tblSale;
$(function () {
    tblSale = $('#data').DataTable({
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
            {"data": "cli.full_name"},
            {"data": "date_joined"},
            {"data": "subtotal"},
            {"data": "iva"},
            {"data": "total"},
            {"data": "methodpay.pay"},
            {"data": "id"},
        ],
        order: [[0, 'desc']],
        columnDefs: [
            {
                targets: [-5, -3, -4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return 'Gs.' + parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
                    buttons += '<a href="/erp/sale/invoice/pdf/'+row.id+'/" target="_blank" class="btn btn-info btn-xs btn-flat"><i class="far fa-file-pdf"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    $('#data tbody')
    .on('click', 'a[rel="details"]', function () {
        var tr = tblSale.cell($(this).closest('td, li')).index();
        var data = tblSale.row(tr.row).data();
        
        $('#tblDet').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_details_prod',
                    'id': data.id
                },
                dataSrc: ""
            },
            columns: [
                {"data": "prod.name"},
                {"data": "prod.cate.name"},
                {"data": "price"},
                {"data": "cant"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [-1, -3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return 'Gs.' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return data;
                    }
                },
            ],
            initComplete: function (settings, json) {
    
            }
        });
        $('#myModalDet').modal('show');

    })
    .on('click', 'a[rel="delete"]', function () {
        var tr = tblSale.cell($(this).closest('td, li')).index();
        var data = tblSale.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, parameters, function () {
                tblSale.ajax.reload();
            });
        });
});
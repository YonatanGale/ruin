var tblBuy;
$(function () {
    tblBuy = $('#data').DataTable({
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
            {"data": "prov.full_name"},
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
                    buttons += '<a href="/erp/buy/invoice/pdf/'+row.id+'/" target="_blank" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    //--------------------f----------------------------------------------------------------------------

    //Modal
    $('#data tbody')
        .on('click', 'a[rel="details"]', function () {
            var tr = tblBuy.cell($(this).closest('td, li')).index();
            var data = tblBuy.row(tr.row).data();
            console.log(data);

           tbldet = $('#tblDet').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_prod',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                paging: false,
                ordering: false,
                info: false,
                searching: false,
                columns: [
                    {"data": "prod.name"},
                    {"data": "price"},
                    {"data": "cant"},
                    {"data": "subtotal"},
                    {"data": "status"},
                    {"data": "status"},
                ],
                columnDefs: [
                    {
                        targets: [-3, -5],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return 'Gs.' + parseFloat(data).toFixed(2);
                        }
                    },
                    {
                        targets: [-4],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return data;
                        }
                    },
                    {
                        targets: [-1],
                        class: 'text-center',
                        render: function (data, type, row) {
                            if (row.status == 'p'){
                                var buttons = '<a href="#" rel="confirm" class="btn btn-success btn-xs"><i class="fas fa-check-square"></i></a> ';
                                return buttons
                            }
                            return 'YA FUE CONFIRMADA';

                        }
                    },
                    {
                        targets: [-2],
                        class: 'text-center',
                        render: function (data, type, row) {
                            if (row.status == 'p'){
                                return '<span class="badge badge-danger">POR CONFIRMAR</span>'
                            }
                            return '<span class="badge badge-success">ENTRAGA CONFIRMADA</span>'

                        }
                    },
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelDet').modal('show');
        })
        .on('click', 'a[rel="delete"]', function () {
            var tr = tblBuy.cell($(this).closest('td, li')).index();
            var data = tblBuy.row(tr.row).data();
                var parameters = new FormData();
                parameters.append('action', 'delete');
                parameters.append('id', data.id);
                submit_with_ajax(window.location.pathname, parameters, function () {
                    tblBuy.ajax.reload();
                });
            });
        
    $('#tblDet tbody')
    .on('click', 'a[rel="confirm"]', function () {
        var tr = tbldet.cell($(this).closest('td, li')).index();
        var data = tbldet.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'confirm_prov');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, parameters, function () {
                location.href = '/erp/buy/list/';
            });
        });
        
});
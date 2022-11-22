var tblProduction;
$(function () {
    tblProduction = $('#data').DataTable({
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
            {"data": "produc.full_name"},
            {"data": "date_joined"},
            {"data": "total"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
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
            var tr = tblProduction.cell($(this).closest('td, li')).index();
            var data = tblProduction.row(tr.row).data();
            console.log(data);

            $('#tblDet').DataTable({
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
                    {"data": "cant"},
                ],
                columnDefs: [
                    {
                        targets: [-1],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return data;
                        }
                    },
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelDet').modal('show');
        })
        .on('click', 'a[rel="delete"]', function () {
            var tr = tblProduction.cell($(this).closest('td, li')).index();
            var data = tblProduction.row(tr.row).data();
                var parameters = new FormData();
                parameters.append('action', 'delete');
                parameters.append('id', data.id);
                submit_with_ajax(window.location.pathname, parameters, function () {
                    tblProduction.ajax.reload();
                });
            });
});
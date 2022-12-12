var tblProducts;
var tblSearchProducts;
var comp = {
    items: {
        produc: '',
        date_joined: '',
        cant: 0.00,
        total: 0,
        products: []
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.products, function (key, value) {
            ids.push(value.id);
        });
        return ids;
    },


    add: function (item) {
        this.items.products.push(item);
        this.list();
    },
    list: function () {

        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "id"},
                {"data": "full_name"},
                {"data": "stock"},
                {"data": "cant"},
            ],
            columnDefs: [
                {
                    //eliminar
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs"><i class="far fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (data == 0) {
                            return '<span class="badge badge-warning">' + data + '</span>'
                        } else return '<span class="badge badge-light">' + data + '</span>'
                    }
                },
                {
                    //cantidad
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cant + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cant"]').TouchSpin({
                    min: 0,
                    max: data.stock,
                    step: 0.1,
                    decimals: 2,
                });

            },
            initComplete: function (settings, json) {

            }
        });
    },
};

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    if(!Number.isInteger(repo.id)){
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">' +
        '<div class="row">' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Nombre/Categoria:</b> ' + repo.full_name + '<br>' +
        '<b>Stock:</b> ' + repo.stock + '<br>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD', 
        date: moment().format("YYYY-MM-DD"), 
        locale: 'es',  
    });

    $("input[name='total']").TouchSpin({
        min: 1,
        max: 100,
        step: 1,
    }).on('change', function () {
        var total = $('input[name="total"]').val();
        console.log(total);
        $('input[name="total"]').val();

    }).val(1);
    
//busqueda de producto
    $('select[name="produc"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_clients'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
    });

    //agregar nuevo producto

    $('.btnAddSupplier').on('click', function () { 
        $('#myModalSupplier').modal('show');
    });

    $('#myModalSupplier').on('hidden.bs.modal', function (e) {
        $('#frmSupplier').trigger('reset');

    })

    $('#frmSupplier').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_supplier');
        submit_with_ajax(window.location.pathname, parameters, function (response) {
                var newOption = new Option(response.full_name, response.id, false, true);
                $('select[name="produc"]').append(newOption).trigger('change');
                $('#myModalSupplier').modal('hide'); 
            });
    });


// busqueda de productos


    //Remover todos los items
    $('.btnRemoveAll').on('click', function () {
        if (comp.items.products.length === 0) return false; 
        //alert_action, control que  esta en static/js/functions
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function () {
            comp.items.products = [];
            comp.list();
        }, function () {

        });
    });

    $('#tblProducts tbody')
        //boton eliminar
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function () {
                comp.items.products.splice(tr.row, 1);
                comp.list();
            }, function () {

            });
        })
        //cantidad
        .on('change', 'input[name="cant"]', function () {
            console.clear();
            var cant = parseFloat($(this).val());
            console.log(cant)
            var tr = tblProducts.cell($(this).closest('td, li')).index(); 
            comp.items.products[tr.row].cant = cant;
        });

    //Boton X del buscador
    $('.btnClearSearch').on('click', function () {
        $('input[name="search"]').val('').focus();
    });

    //buscar producto desde la venta

    $('.btnSearchProducts').on('click', function () {
        tblSearchProducts = $('#tblSearchProducts').DataTable( {
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action':'search_products',
                    'ids': JSON.stringify(comp.get_ids()),
                    'term': $('select[name="search"]').val()
                },
                dataSrc: ""
            },
            columns: [
                { "data": "name"},
                { "data": "stock"},
                { "data": "stock"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="#" rel="add" class="btn btn-success btn-xs btn-flat"><i class="fas fa-plus"></i></a> ';
                        return buttons
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '<span class="badge badge-secondary">'+data+'</span>'
                    }
                },
            ],
            initComplete: function(settings, json) {
            
              }
            });
        $('#myModalProduct').modal('show');
    });

    $('#tblSearchProducts tbody')
        .on('click', 'a[rel="add"]', function () {
        var tr = tblSearchProducts.cell($(this).closest('td, li')).index();
        var product = tblSearchProducts.row(tr.row).data();
        product.cant = 1;
        comp.add(product);
        tblSearchProducts.row( $(this).parents('tr') ).remove().draw();
    });

    // evento guardar
    $('#frmBuy').on('submit', function (e) {
        e.preventDefault();

        //validaciónes para los items
        if (comp.items.products.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }
        comp.items.total = $('input[name="total"]').val();
        comp.items.date_joined = $('input[name="date_joined"]').val();
        comp.items.produc = $('select[name="produc"]').val();

        var parameters = new FormData();

        parameters.append('action', $('input[name="action"]').val());
        parameters.append('comp', JSON.stringify(comp.items));
        submit_with_ajax(window.location.pathname, parameters, function () {
                location.href = '/erp/production/list';
            });
    });

    $('select[name="search"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_autocomplete',
                    ids: JSON.stringify(comp.get_ids())
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        if(!Number.isInteger(data.id)){
            return false;
        }
        data.cant = 1;
        comp.add(data);
        $(this).val('').trigger('change.select2');
    });


    comp.list(); 
});
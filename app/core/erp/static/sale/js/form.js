var tblProducts;
var tblSearchProducts;

var vents = {
    items: {
        cli: '',
        methodpay: '',
        typfund: '',
        date_joined: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        products: [],
        funds: []
    },    
    get_ids: function () { //para obtener el id y que el producto no se repita en el detalle de venta
        var ids = [];
        $.each(this.items.products, function (key, value) {
            ids.push(value.id);
        });
        return ids;
    },
    calculate_invoice: function(){
        var subtotal = 0.00;
        var iva = $('input[name="iva"]').val();
        $.each(this.items.products, function(pos, dict){
            dict.subtotal = dict.cant * parseFloat(dict.price)
            subtotal+=dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="ivacal"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function(item){
        this.items.products.push(item);
        this.list();
    },
    list: function (){
        this.calculate_invoice();

        tblProducts = $('#tblProducts').DataTable( {
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                { "data": "id"},
                { "data": "full_name"},
                { "data": "stock"},
                { "data": "price"},
                { "data": "cant"},
                { "data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs"><i class="far fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-4],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '<span class="badge badge-secondary">'+data+'</span>'
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Gs'+parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="'+row.cant+'">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Gs'+parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback( row, data, displayNum, displayIndex, dataIndex ){
                
                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: data.stock,
                    step: 1
                })
            },
            initComplete: function(settings, json) {
            
              }
            });
        console.clear();
        console.log(this.items);
        console.log(this.get_ids());
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
        '<b>Precio:</b> <span class="badge badge-warning">Gs.' + repo.price + '</span>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        lenguaje: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
    });

    $("input[name='iva']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.01,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).on('change', function () {
        vents.calculate_invoice();
    }).val(0.05);

    //buscador de clientes
    $('select[name="cli"]').select2({
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

    $('.btnAddClient').on('click', function () {
        $('#myModalClient').modal('show');
    });

    $('#myModalClient').on('hidden.bs.modal', function (e) {
        $('#formClient').trigger('reset');
      })

    $('#formClient').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_client');
        submit_with_ajax(window.location.pathname, parameters, function (response) {
            //console.log(response);
            var newOption = new Option(response.full_name, response.id, false, true);
            $('select[name="cli"]').append(newOption).trigger('change');
            $('#myModalClient').modal('hide');
        });
    });

    
    var select_typeFunds = $('select[name="typfund"]');

    $('select[name="methodpay"]').on('change', function () {
        var id = $(this).val();
        var options = '<option value="">--------------</option>';
        if (id == '') {
            select_typeFunds.html(options);
            return false;
        }
        $.ajax({
            url: window.location.pathname, //window.location.pathname
            type: 'POST',
            data: {
                'action': 'search_methodpay',
                'id': id
            },
            dataType: 'json',
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                select_typeFunds.html('').select2({
                    theme: "bootstrap4",
                    lenguaje: 'es',
                    data: data
                });
                // $.each(data, function(key, value) {
                //     options+='<option value="'+value.id+'">'+value.name+'</option>'
                // });
                return false;
            }
            message_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
            //select_typeFunds.html(options);
        });
    });

    select_typeFunds.on('change', function () {
        var value = select_typeFunds.select2('data')[0];
        console.log(value);
    });
    //     theme: "bootstrap4",
    //     language: 'es',
    //     allowClear: true,
    //     ajax: {
    //         delay: 250,
    //         type: 'POST',
    //         url: window.location.pathname,
    //         data: function (params) {
    //             var queryParameters = {
    //                 term: params.term,
    //                 action: 'search_methodpay'
    //             }
    //             return queryParameters;
    //         },
    //         processResults: function (data) {
    //             return {
    //                 results: data
    //             };
    //         },
    //     },
    //     placeholder: 'Ingrese una descripción',
    //     minimumInputLength: 1,
    // });
    //buscador de productos
    // $('input[name="search"]').autocomplete({
    //     source: function (request, response) {
    //         $.ajax({
    //             url: window.location.pathname,
    //             type: 'POST',
    //             data: {
    //                 'action': 'search_products',
    //                 'term': request.term,
    //                 ids: JSON.stringify(vents.get_ids())
    //             },
    //             dataType: 'json',
    //         }).done(function (data) {
    //             response(data);
    //         }).fail(function (jqXHR, textStatus, errorThrown) {
    //             //alert(textStatus + ': ' + errorThrown);
    //         }).always(function (data) {

    //         });
    //     },
    //     delay: 500,
    //     minLength: 1,
    //     select: function (event, ui) {
    //         event.preventDefault();
    //         console.clear();
    //         ui.item.cant = 1;
    //         ui.item.subtotal = 0.00;
    //         console.log(vents.items);
    //         vents.add(ui.item);
    //         $(this).val('');
    //     }
    // });

    $('.btnRemoveAll').on('click', function () {
        alert_action('Notification', '¿Desea vaciar el carrito?', function () {
        if(vents.items.products == 0) return false;
            vents.items.products = [];
            vents.list();
        }, function () {

        });
    });

    //event cantidad
    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            vents.items.products.splice(tr.row, 1);
            vents.list();
        })
        .on('change', 'input[name="cant"]', function () {
        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        vents.items.products[tr.row].cant = cant;
        vents.calculate_invoice();
        $('td:eq(5)',tblProducts.row(tr.row).node()).html( 'Gs.'+vents.items.products[tr.row].subtotal.toFixed(2));

    });

    $('.btnClearSearch').on('click', function () {
        $('input[name="search"]').val('').focus();
    });

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
                    'ids': JSON.stringify(vents.get_ids()),
                    'term': $('select[name="search"]').val()
                },
                dataSrc: ""
            },
            columns: [
                { "data": "full_name"},
                { "data": "stock"},
                { "data": "price"},
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
                    targets: [-3],
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
        product.subtotal = 0.00;
        vents.add(product);
        tblSearchProducts.row( $(this).parents('tr') ).remove().draw();
    });

    //event submit
    $('#formSale').on('submit', function (e) {
        e.preventDefault();

        if(vents.items.products.length === 0){
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.date_joined = $('input[name="date_joined"]').val();
        vents.items.cli = $('select[name="cli"]').val();
        vents.items.methodpay = $('select[name="methodpay"]').val();
        vents.items.typfund = $('select[name="typfund"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, parameters, function (response) {
            alert_action('Notification', '¿Desea imprimir la factura?', function () {
                window.open('/erp/sale/invoice/pdf/'+response.id+'/', '_blank');
                location.href = '/erp/sale/list/';
            }, function () {
                location.href = '/erp/sale/list/';
            })
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
                    ids: JSON.stringify(vents.get_ids())
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
        data.subtotal = 0.00;
        vents.add(data);
        $(this).val('').trigger('change.select2');
    });

    vents.list();
});
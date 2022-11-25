 var tblType;
 var tblfund;
 var modal_title;

 function getData(){
    tblfund = $('#tblfund').DataTable({
        responsive: true,
        autoWidth: false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata',
            },
            dataSrc: "",
        },
        columns: [
            {"data": "id"},
            {"data": "amount"},
            {"data": "typeMove"},
            {"data": "typeF.name"},
            {"data": "methodpay.pay"},
            {"data": "payNro"},
            {"data": "payowner"},
            {"data": "date_joined"},
        ],
        columnDefs: [
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return 'Gs.' + parseFloat(data).toLocaleString("es-AR");
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
        
    tblType= $('#tblType').DataTable({
            responsive: true,
            autoWidth: false,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'TypeList',
                },
                dataSrc: "",
            },
            order: false,
            info: false,
            paging: false,
            searching: false,
            columns: [
                {"data": "name"},
                {"data": "impo"},
            ],
            columnDefs: [
                {
                    targets: [1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        if(row.impo == 0){
                            return '';
                        }
                        return 'Gs.' + parseFloat(data).toLocaleString("es-AR");
                    }
                },
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        if(row.name == 'Caja/Banco'){
                            return '';
                        }
                        return data;
                    }
                },
            ],
            initComplete: function (settings, json) {
    
            }
        });
}

$(function () {

    modal_title = $('.modal-title');

    getData();


    $('.btnwithdraw').on('click', function () {
        $('input[name="action"]').val('addwithdraw');
        modal_title.find('span').html('Retirar de caja');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalwithdraw').modal('show');
    });

    $('.addCargar').on('click', function () {
        $('input[name="action"]').val('addCargar');
        modal_title.find('span').html('Carga de caja');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalwithdraw').modal('show');
    });

    $('.btnCierre').on('click', function () {
        $('input[name="action"]').val('addcierre');
        modal_title.find('span').html('Cierre de caja');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalcierre').modal('show');
        
    });

    $('.btnAper').on('click', function () {
        $('input[name="action"]').val('addapertura');
        modal_title.find('span').html('Apertura de caja');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalcierre').modal('show');
        
    });

    // $('.btnCierre').on('click', function () {
    //     $('input[name="action"]').val('addcierre');
    //      var date_joined = datetime.now;
    //      if ()
    //     $('#form').on('submit', function (e) {
    //         e.preventDefault();
    //         cierre.date_joined = $('input[name="date_joined"]').val(date_joined);
    //         cierre.caja = $('input[name="caja"]').val();
    //         cierre.banco = $('input[name="banco"]').val();
    
    //         var parameters = $(this).serializeArray();
    //         alert_jqueryconfirm(window.location.pathname, parameters, function () {
    //             location.href = '/erp/funds/list/';
    //         });
    //     });
    // });

    $('#formwithdraw').on('submit', function (e) {
        e.preventDefault();
        var parameters = $(this).serializeArray();
        alert_jqueryconfirm(window.location.pathname, parameters, function () {
            location.href = '/erp/funds/list/';
        });
    });

    $('#frmCaja').on('submit', function (e) {
        e.preventDefault();
        var parameters = $(this).serializeArray();
        alert_jqueryconfirm(window.location.pathname, parameters, function () {
            $('#myModalcierre').modal('hide');
        });
    });
   
});
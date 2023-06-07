var date_ranger = null;
var date_now = new moment().format('YYYY-MM-DD');

function generate_report () {
    var parameters = {
        'action': 'search_report',
        'start_date': date_now,
        'end_date': date_now
    };

    if(date_ranger !== null){
        parameters['start_date'] = date_ranger.startDate.format('YYYY-MM-DD');
        parameters['end_date'] = date_ranger.endDate.format('YYYY-MM-DD');
    }

    $(function (){
        $('#data').DataTable( {
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: parameters,
                dataSrc: ""
            },
            order: false,
            paging: false,
            ordering: false,
            info: false,
            searching: false,
            dom: 'Bfrtip',
            buttons: [
                {
                    extend: 'excelHtml5',
                    text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
                    titleAttr: 'Excel',
                    className: 'btn btn-success btn-flat btn-xs'
                },
                {
                    extend: 'pdfHtml5',
                    text: 'Descargar Pdf <i class="fas fa-file-pdf"></i>',
                    titleAttr: 'PDF',
                    className: 'btn btn-danger btn-flat btn-xs',
                    download: 'open',
                    orientation: 'landscape',
                    pageSize: 'LEGAL',
                    customize: function (doc) {
                        doc.styles = {
                            header: {
                                fontSize: 18,
                                bold: true,
                                alignment: 'center'
                            },
                            subheader: {
                                fontSize: 13,
                                bold: true
                            },
                            quote: {
                                italics: true
                            },
                            small: {
                                fontSize: 8
                            },
                            tableHeader: {
                                bold: true,
                                fontSize: 11,
                                color: 'white',
                                fillColor: '#2d4154',
                                alignment: 'center'
                            }
                        };
                        doc.content[1].table.widths = ['5%','15%','15%','15%','15%','15%'];
                        doc.content[1].margin = [0, 35, 0, 0];
                        doc.content[1].layout = {};
                        doc['footer'] = (function (page, pages) {
                            return {
                                columns: [
                                    {
                                        alignment: 'left',
                                        text: ['Fecha de creación: ', {text: date_now}]
                                    },
                                    {
                                        alignment: 'right',
                                        text: ['página ', {text: page.toString()}, ' de ', {text: pages.toString()}]
                                    }
                                ],
                                margin: 20
                            }
                        });
    
                    }
                }
            ],
            // columns: [
            //     { "data": "id"},
            //     { "data": "name"},
            //     { "data": "id"},
            // ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Gs'+ parseFloat(data).toLocaleString("es-AR");
                    }
                },
            ],
            initComplete: function(settings, json) {
            
              }
            });
    });
}

$(function () {
    $('input[name="date_ranger"]').daterangepicker({
        locale : {
            format: 'YYYY-MM-DD'

        }
    }).on('apply.daterangepicker', function(ev, picker) {
        date_ranger = picker;
        generate_report();
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_now);
        $(this).data('daterangepicker').setEndDate(date_now);
        date_ranger = picker;
        generate_report();
    });


    generate_report();
});
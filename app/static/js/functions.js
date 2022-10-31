function alert_jqueryconfirm(){
    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: '¿Estas seguro de realizar la siguiente accion?',
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    
                }
            },
        }
    })

}
function message_error(obj) {
    var html ='';
    if(typeof (obj) === 'object'){
        html = '<ul>';
        $.each(obj, function (key, value) {
            html+='<li>'+key+': '+value+'</li>';
        });
        html+='</ul>';
    }
    else{
        html = '<p>'+obj+'</p>';
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}
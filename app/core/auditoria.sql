-- TRIGGERS PARA SQLITE
-------------------/-----------------/--------------------------/------------------------/----------------
--AUDITORIA INSERT CATEGORYMATERIALS
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CATEGORYMATERIALS
AFTER INSERT ON erp_categorymaterials
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_categorymaterials', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.unity, '')|| ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ), 
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE CATEGORYMATERIALS
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CATEGORYMATERIALS
AFTER UPDATE ON erp_categorymaterials
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_categorymaterials', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.unity, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.unity, '')|| ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE CATEGORYMATERIALS
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_CATEGORYMATERIALS
AFTER DELETE ON erp_categorymaterials
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_categorymaterials', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.unity, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---

--AUDITORIA INSERT BUY

CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_BUY
AFTER INSERT ON erp_buy
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_buy', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.iva, '')|| ',' || IFNULL(NEW.total, '')|| ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.prov_id, '') || ',' || IFNULL(NEW.methodpay_id, '')|| ',' || IFNULL(NEW.typfund_id, '')|| ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ), 
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE BUY
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_BUY
AFTER UPDATE ON erp_buy
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_buy', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.iva, '')|| ',' || IFNULL(OLD.total, '')|| ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.prov_id, '') || ',' || IFNULL(OLD.methodpay_id, '')|| ',' || IFNULL(OLD.typfund_id, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || OLD.user_create|| ',' || IFNULL(OLD.user_update, '')  ),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.iva, '')|| ',' || IFNULL(NEW.total, '')|| ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.prov_id, '') || ',' || IFNULL(NEW.methodpay_id, '')|| ',' || IFNULL(NEW.typfund_id, '')|| ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ), 
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE BUY
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_BUY
AFTER DELETE ON erp_buy
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_buy', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.iva, '')|| ',' || IFNULL(OLD.total, '')|| ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.prov_id, '') || ',' || IFNULL(OLD.methodpay_id, '')|| ',' || IFNULL(OLD.typfund_id, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || OLD.user_create|| ',' || IFNULL(OLD.user_update, '')  ),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT CATEGORY
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CATEGORY
AFTER INSERT ON erp_category
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_category', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE CATEGORY

CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CATEGORY
AFTER UPDATE ON erp_category
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_category', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE CATEGORY

CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_CATEGORY
AFTER DELETE ON erp_category
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_category', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT CIERRECAJA
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CIERRECAJA
AFTER INSERT ON erp_cierrecaja
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_cierrecaja', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.typeF_id, '') || ',' || IFNULL(NEW.tot, '') || ',' || IFNULL(NEW.estado, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE CIERRECAJA

CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CIERRECAJA
AFTER UPDATE ON erp_cierrecaja
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_cierrecaja', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.typeF_id, '') || ',' || IFNULL(OLD.tot, '') || ',' || IFNULL(OLD.estado, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.typeF_id, '') || ',' || IFNULL(NEW.tot, '') || ',' || IFNULL(NEW.estado, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT CLIENTE
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CLIENT
AFTER INSERT ON erp_client
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_client', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.names, '') || ',' || IFNULL(NEW.surnames, '') || ',' || IFNULL(NEW.ci, '') || ',' || IFNULL(NEW.Birthday, '') || ',' || IFNULL(NEW.addres, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_creation_id, '')|| ',' || IFNULL(NEW.user_update_id, '')  ),  
        NEW.user_creation_id, 
        date('now'));
END;

--AUDITORIA UPDATE CLIENTE
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CLIENTE
AFTER UPDATE ON erp_client
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_client', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.names, '') || ',' || IFNULL(OLD.surnames, '') || ',' || IFNULL(OLD.Birthday, '') || ',' || IFNULL(OLD.addres, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_creation_id, '')|| ',' || IFNULL(OLD.user_update_id, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.names, '') || ',' || IFNULL(NEW.surnames, '') || ',' || IFNULL(NEW.Birthday, '') || ',' || IFNULL(NEW.addres, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_creation_id, '')|| ',' || IFNULL(NEW.user_update_id, '')),
    NEW.user_update_id, 
    date('now')
    );
END;

--AUDITORIA DELETE CLIENTE
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_CLIENT
AFTER DELETE ON erp_client
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_client', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.names, '') || ',' || IFNULL(OLD.surnames, '') || ',' || IFNULL(OLD.ci, '') || ',' || IFNULL(OLD.Birthday, '') || ',' || IFNULL(OLD.addres, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_creation_id, '')|| ',' || IFNULL(OLD.user_update_id, '')),
    NULL,
    OLD.user_update_id, 
    date('now')
    );
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT DETBUY
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_DET_BUY
AFTER INSERT ON erp_detbuy
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_detbuy', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.price, '') || ',' || IFNULL(NEW.cant, '') || ',' || IFNULL(NEW.subtotal, '') || ',' || IFNULL(NEW.buy_id, '') || ',' || IFNULL(NEW.prod_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT PRODUCTIONS
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_PRODUCTION
AFTER INSERT ON erp_production
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_production', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.produc_id, '') || ',' || IFNULL(NEW.total, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE PRODUCTIONS
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_PRODUCTION
AFTER UPDATE ON erp_production
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_production', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.produc_id, '') || ',' || IFNULL(OLD.total, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.produc_id, '') || ',' || IFNULL(NEW.total, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE PRODUCTIONS
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_PRODUCTION
AFTER DELETE ON erp_production
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_production', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.produc_id, '') || ',' || IFNULL(OLD.total, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

--AUDITORIA INSERT DETPRODUCTIONS
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_DETPRODUCTION
AFTER INSERT ON erp_detproduction
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_detproduction', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.cant, '') || ',' || IFNULL(NEW.prod_id, '') || ',' || IFNULL(NEW.crea_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT SALE
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_SALE
AFTER INSERT ON erp_sale
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_sale', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.subtotal, '') || ',' || IFNULL(NEW.iva, '') || ',' || IFNULL(NEW.total, '') || ',' || IFNULL(NEW.cli_id, '') || ',' || IFNULL(NEW.methodpay_id, '') || ',' || IFNULL(NEW.typfund_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE SALE
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_SALE
AFTER UPDATE ON erp_sale
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_sale', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.subtotal, '') || ',' || IFNULL(OLD.iva, '') || ',' || IFNULL(OLD.total, '') || ',' || IFNULL(OLD.cli_id, '') || ',' || IFNULL(OLD.methodpay_id, '') || ',' || IFNULL(OLD.typfund_id, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.subtotal, '') || ',' || IFNULL(NEW.iva, '') || ',' || IFNULL(NEW.total, '') || ',' || IFNULL(NEW.cli_id, '') || ',' || IFNULL(NEW.methodpay_id, '') || ',' || IFNULL(NEW.typfund_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE SALE
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_SALE
AFTER DELETE ON erp_sale
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_sale', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.subtotal, '') || ',' || IFNULL(OLD.iva, '') || ',' || IFNULL(OLD.total, '') || ',' || IFNULL(OLD.cli_id, '') || ',' || IFNULL(OLD.methodpay_id, '') || ',' || IFNULL(OLD.typfund_id, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

--AUDITORIA INSERT DETSALE
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_DETSALE
AFTER INSERT ON erp_detsale
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_detsale', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.price, '') || ',' || IFNULL(NEW.cant, '') || ',' || IFNULL(NEW.subtotal, '') || ',' || IFNULL(NEW.prod_id, '') || ',' || IFNULL(NEW.sale_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT FUND
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_fund
AFTER INSERT ON erp_fund
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_fund', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.amount, '') || ',' || IFNULL(NEW.typeMove, '') || ',' || IFNULL(NEW.payNro, '') || ',' || IFNULL(NEW.payowner, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.closing_id, '') || ',' || IFNULL(NEW.typeF_id, '') || ',' || IFNULL(NEW.sale_id, '') || ',' || IFNULL(NEW.methodpay_id, '') || ',' || IFNULL(NEW.buy_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE FUND
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_FUND
AFTER UPDATE ON erp_fund
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_fund', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.amount, '') || ',' || IFNULL(OLD.typeMove, '') || ',' || IFNULL(OLD.payNro, '') || ',' || IFNULL(OLD.payowner, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.closing_id, '') || ',' || IFNULL(OLD.typeF_id, '') || ',' || IFNULL(OLD.sale_id, '') || ',' || IFNULL(OLD.methodpay_id, '') || ',' || IFNULL(OLD.buy_id, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.amount, '') || ',' || IFNULL(NEW.typeMove, '') || ',' || IFNULL(NEW.payNro, '') || ',' || IFNULL(NEW.payowner, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.closing_id, '') || ',' || IFNULL(NEW.typeF_id, '') || ',' || IFNULL(NEW.sale_id, '') || ',' || IFNULL(NEW.methodpay_id, '') || ',' || IFNULL(NEW.buy_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT MATERIALS
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_MATERIALS
AFTER INSERT ON erp_materials
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_materials', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.stock, '') || ',' || IFNULL(NEW.price, '') || ',' || IFNULL(NEW.cate_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE MATERIALS
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_MATERIALS
AFTER UPDATE ON erp_materials
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_materials', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.stock, '') || ',' || IFNULL(OLD.cate_id, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.stock, '') || ',' || IFNULL(NEW.cate_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE MATERIALS
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_MATERIALS
AFTER DELETE ON erp_materials
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_materials', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.stock, '') || ',' || IFNULL(OLD.price, '') || ',' || IFNULL(OLD.cate_id, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT PRODUCT
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_PRODUCTS
AFTER INSERT ON erp_product
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_product', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.cate_id, '') || ',' || IFNULL(NEW.price, '') || ',' || IFNULL(NEW.stock, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE PRODUCT
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_PRODUCTS
AFTER UPDATE ON erp_product
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_product', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.cate_id, '') || ',' || IFNULL(OLD.price, '') || ',' || IFNULL(OLD.stock, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.cate_id, '') || ',' || IFNULL(NEW.price, '') || ',' || IFNULL(NEW.stock, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE PRODUCT
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_PRODUCTS
AFTER DELETE ON erp_product
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_product', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.cate_id, '') || ',' || IFNULL(OLD.price, '') || ',' || IFNULL(OLD.stock, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;


------------------/--------------------------------/---------------------------------/---------------------------------/---


--AUDITORIA INSERT SUPPLIER
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_SUPPLIER
AFTER INSERT ON erp_supplier
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_supplier', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.names, '') || ',' || IFNULL(NEW.surnames, '') || ',' || IFNULL(NEW.phone, '') || ',' || IFNULL(NEW.address, '') || ',' || IFNULL(NEW.ci, '') || ',' || IFNULL(NEW.email, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_creation1_id|| ',' || IFNULL(NEW.user_update1_id, '') ),  
        NEW.user_creation1_id, 
        date('now'));
END;

--AUDITORIA UPDATE SUPPLIER
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_SUPPLIER
AFTER UPDATE ON erp_supplier
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_supplier', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.names, '') || ',' || IFNULL(OLD.surnames, '') || ',' || IFNULL(OLD.phone, '') || ',' || IFNULL(OLD.address, '') || ',' || IFNULL(OLD.ci, '') || ',' || IFNULL(OLD.email, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_creation1_id, '')|| ',' || IFNULL(OLD.user_update1_id, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.names, '') || ',' || IFNULL(NEW.surnames, '') || ',' || IFNULL(NEW.phone, '') || ',' || IFNULL(NEW.address, '') || ',' || IFNULL(NEW.ci, '') || ',' || IFNULL(NEW.email, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_creation1_id, '')|| ',' || IFNULL(NEW.user_update1_id, '')),
    NEW.user_update1_id, 
    date('now')
    );
END;

--AUDITORIA DELETE SUPPLIER
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_SUPPLIER
AFTER DELETE ON erp_supplier
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_supplier', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.names, '') || ',' || IFNULL(OLD.surnames, '') || ',' || IFNULL(OLD.phone, '') || ',' || IFNULL(OLD.address, '') || ',' || IFNULL(OLD.ci, '') || ',' || IFNULL(OLD.email, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_creation1_id, '')|| ',' || IFNULL(OLD.user_update1_id, '')),
    NULL,
    OLD.user_update1_id, 
    date('now')
    );
END;

